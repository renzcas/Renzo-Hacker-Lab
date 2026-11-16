from pattern_hunter.models.signal import Signal


def test_signal_creation():

    signal = Signal(
        signal_type="FREQUENCY_SPIKE",
        confidence=90.0,
        risk_score=50.0,
        source_events=10,
        summary="Spike detected",
    )

    assert signal.signal_type == "FREQUENCY_SPIKE"
    assert signal.confidence == 90.0


def test_signal_to_dict():

    signal = Signal(
        signal_type="TEST",
        confidence=80.0,
        risk_score=40.0,
        source_events=5,
        summary="Test Signal",
    )

    result = signal.to_dict()

    assert result["signal_type"] == "TEST"
    assert result["source_events"] == 5