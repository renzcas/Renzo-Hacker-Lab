from pattern_hunter.models.event import Event


def test_event_creation():

    event = Event(
        timestamp="2026-11-16T12:00:00",
        source="telemetry",
        category="SYSTEM",
        event_type="agent_restart",
        severity=3.0,
    )

    assert event.source == "telemetry"
    assert event.category == "SYSTEM"
    assert event.event_type == "agent_restart"
    assert event.severity == 3.0


def test_event_to_dict():

    event = Event(
        timestamp="2026",
        source="lab",
        category="TEST",
        event_type="sample",
        severity=1.0,
    )

    result = event.to_dict()

    assert result["source"] == "lab"
    assert result["category"] == "TEST"