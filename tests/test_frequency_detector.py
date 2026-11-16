from pattern_hunter.models.event import Event
from pattern_hunter.detector.frequency_detector import (
    FrequencyDetector,
)


def test_frequency_spike():

    detector = FrequencyDetector()

    events = []

    for _ in range(6):

        events.append(
            Event(
                timestamp="2026",
                source="telemetry",
                category="AUTH",
                event_type="login_failure",
                severity=1.0,
            )
        )

    signals = detector.analyze(events)

    assert len(signals) == 1

    assert (
        signals[0].signal_type
        == "FREQUENCY_SPIKE"
    )


def test_no_spike():

    detector = FrequencyDetector()

    events = []

    for _ in range(3):

        events.append(
            Event(
                timestamp="2026",
                source="telemetry",
                category="AUTH",
                event_type="login_failure",
                severity=1.0,
            )
        )

    signals = detector.analyze(events)

    assert len(signals) == 0