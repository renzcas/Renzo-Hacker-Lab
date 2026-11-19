import importlib.util
import pathlib
import unittest

_SPEC = importlib.util.spec_from_file_location(
    "simcore_monitor",
    pathlib.Path(__file__).resolve().parent.parent
    / "Renzo-Hacker-Lab"
    / "blue-team"
    / "detection"
    / "simcore_monitor.py",
)
assert _SPEC and _SPEC.loader
simcore_monitor = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(simcore_monitor)


class TestSimCoreMonitor(unittest.TestCase):
    def test_calm_spine_event_produces_no_alerts(self) -> None:
        spine_event = {
            "schemaVersion": "1.0.0",
            "eventId": "simcore-tick-14-agent-4",
            "worldId": "renzoverse.simcore.primary",
            "sequence": 14,
            "tick": 14,
            "occurredAt": "2026-11-19T10:30:00+00:00",
            "eventType": "simcore.agent.state",
            "sourceModuleId": "Renzo-SimCore",
            "payload": {
                "agentId": 4,
                "agentName": "Keeper",
                "role": "Keeper",
                "goalSatisfied": False,
                "memorySize": 12,
                "beliefs": {
                    "threat": 0.20,
                    "fear": 0.00,
                    "panic": 0.00,
                    "trust": 0.80,
                    "calm": 0.98,
                },
                "metrics": {"resilience": 0.98},
            },
        }
        self.assertEqual(simcore_monitor.evaluate_simcore_posture(spine_event), [])

    def test_high_panic_and_low_resilience_emit_integration_contract_alerts(self) -> None:
        stressed_event = {
            "schemaVersion": "1.0.0",
            "eventId": "simcore-tick-21-agent-2",
            "worldId": "renzoverse.simcore.primary",
            "sequence": 21,
            "tick": 21,
            "occurredAt": "2026-11-19T10:31:00+00:00",
            "eventType": "simcore.agent.state",
            "sourceModuleId": "Renzo-SimCore",
            "payload": {
                "agentId": 2,
                "agentName": "Scout",
                "role": "Scout",
                "goalSatisfied": False,
                "memorySize": 18,
                "beliefs": {
                    "threat": 0.88,
                    "fear": 0.85,
                    "panic": 0.92,
                    "trust": 0.25,
                    "calm": 0.15,
                },
                "metrics": {"resilience": 0.15},
            },
        }
        alerts = simcore_monitor.evaluate_simcore_posture(stressed_event)
        codes = [a["payload"]["alertCode"] for a in alerts]
        self.assertEqual(codes, ["LOW_RESILIENCE", "PANIC_SPIKE", "THREAT_ELEVATED"])
        for alert in alerts:
            self.assertEqual(alert["contract_version"], "1")
            self.assertEqual(alert["source"], "Renzo-Hacker-Lab.blue-team")
            self.assertEqual(alert["type"], "blue_team.posture_alert")
            self.assertEqual(alert["correlation_id"], "renzoverse.simcore.primary:tick-21")

    def test_rejects_unsupported_major_contract_version(self) -> None:
        with self.assertRaises(simcore_monitor.ContractVersionError):
            simcore_monitor.evaluate_simcore_posture(
                {
                    "contract_version": "2",
                    "event_id": "bad-1",
                    "occurred_at": "2026-11-19T10:31:00+00:00",
                    "source": "Renzo-SimCore",
                    "type": "simcore.agent.state",
                    "payload": {},
                }
            )


if __name__ == "__main__":
    unittest.main()
