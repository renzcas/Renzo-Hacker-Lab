"""Read-only blue-team posture monitor for Renzo-SimCore Spine events."""

from __future__ import annotations

import json
import sys
from collections.abc import Iterable, Mapping
from datetime import datetime, timezone
from typing import Any


class ContractVersionError(ValueError):
    """Raised when an incoming event envelope uses an unsupported major version."""


def _check_major_version(version_value: Any, field_name: str) -> None:
    if not isinstance(version_value, str) or not version_value.strip():
        raise ContractVersionError(f"Missing or invalid {field_name}: {version_value!r}")
    major = version_value.split(".", 1)[0].strip()
    if major != "1":
        raise ContractVersionError(
            f"Unsupported major contract version in {field_name}: {version_value!r}"
        )


def normalize_simcore_event(event: Mapping[str, Any]) -> dict[str, Any]:
    """Normalize either a Renzoverse Spine event_contract or Hacker-Lab envelope."""
    if not isinstance(event, Mapping):
        raise ValueError("Incoming event must be a JSON object.")

    if "schemaVersion" in event:
        _check_major_version(event.get("schemaVersion"), "schemaVersion")
        event_id = event.get("eventId")
        occurred_at = event.get("occurredAt")
        source = event.get("sourceModuleId", "Renzo-SimCore")
        event_type = event.get("eventType")
        world_id = event.get("worldId", "renzoverse.simcore.primary")
        tick = event.get("tick")
        correlation_id = f"{world_id}:tick-{tick}" if tick is not None else world_id
    else:
        _check_major_version(event.get("contract_version"), "contract_version")
        event_id = event.get("event_id")
        occurred_at = event.get("occurred_at")
        source = event.get("source")
        event_type = event.get("type")
        correlation_id = event.get("correlation_id")

    for name, val in (
        ("event_id", event_id),
        ("occurred_at", occurred_at),
        ("source", source),
        ("type", event_type),
    ):
        if not isinstance(val, str) or not val.strip():
            raise ValueError(f"Missing required envelope field: {name}")

    payload = event.get("payload")
    if not isinstance(payload, Mapping):
        raise ValueError("Event payload must be a JSON object.")

    return {
        "contract_version": "1",
        "event_id": event_id,
        "occurred_at": occurred_at,
        "source": source,
        "type": event_type,
        "correlation_id": correlation_id,
        "payload": dict(payload),
    }


def evaluate_simcore_posture(
    event: Mapping[str, Any],
    *,
    min_resilience: float = 0.40,
    max_panic: float = 0.80,
    max_threat: float = 0.75,
) -> list[dict[str, Any]]:
    """Analyze a simcore.agent.state event read-only and emit INTEGRATION_CONTRACT alerts."""
    envelope = normalize_simcore_event(event)
    if envelope["type"] != "simcore.agent.state":
        return []

    payload = envelope["payload"]
    beliefs = payload.get("beliefs")
    metrics = payload.get("metrics")
    if not isinstance(beliefs, Mapping) or not isinstance(metrics, Mapping):
        raise ValueError("simcore.agent.state payload requires object fields beliefs and metrics.")

    agent_name = str(payload.get("agentName") or payload.get("agent") or "unknown")
    agent_id = payload.get("agentId")
    role = str(payload.get("role") or "unknown")

    triggered: list[tuple[str, str, float, float]] = []
    resilience = metrics.get("resilience")
    if isinstance(resilience, (int, float)) and not isinstance(resilience, bool):
        if float(resilience) < min_resilience:
            triggered.append(("LOW_RESILIENCE", "warning", float(resilience), min_resilience))

    panic = beliefs.get("panic")
    if isinstance(panic, (int, float)) and not isinstance(panic, bool):
        if float(panic) > max_panic:
            triggered.append(("PANIC_SPIKE", "critical", float(panic), max_panic))

    threat = beliefs.get("threat")
    if isinstance(threat, (int, float)) and not isinstance(threat, bool):
        if float(threat) > max_threat:
            triggered.append(("THREAT_ELEVATED", "warning", float(threat), max_threat))

    now_iso = datetime.now(timezone.utc).isoformat()
    alerts: list[dict[str, Any]] = []
    for code, severity, observed, threshold in triggered:
        alert_envelope: dict[str, Any] = {
            "contract_version": "1",
            "event_id": f"{envelope["event_id"]}:{code.lower()}",
            "occurred_at": now_iso,
            "source": "Renzo-Hacker-Lab.blue-team",
            "type": "blue_team.posture_alert",
            "payload": {
                "alertCode": code,
                "severity": severity,
                "agentId": agent_id,
                "agentName": agent_name,
                "role": role,
                "observed": observed,
                "threshold": threshold,
                "sourceEventId": envelope["event_id"],
            },
        }
        if envelope.get("correlation_id"):
            alert_envelope["correlation_id"] = envelope["correlation_id"]
        alerts.append(alert_envelope)
    return alerts


def process_ndjson_stream(lines: Iterable[str]) -> list[dict[str, Any]]:
    """Read-only NDJSON consumer returning all posture alerts across a stream."""
    all_alerts: list[dict[str, Any]] = []
    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        record = json.loads(stripped)
        all_alerts.extend(evaluate_simcore_posture(record))
    return all_alerts


if __name__ == "__main__":
    for alert in process_ndjson_stream(sys.stdin):
        print(json.dumps(alert, separators=(",", ":")))
