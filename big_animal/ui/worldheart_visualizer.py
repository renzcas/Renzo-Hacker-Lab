def render_worldheart_waveform(pulse):
    """
    ASCII waveform visualizer for the worldheart pulse.
    Converts pulse into a horizontal bar with symbolic rhythm.
    """

    # Normalize pulse into a range
    normalized = max(-5.0, min(5.0, pulse))

    # Map pulse to bar length
    length = int((normalized + 5) * 5)  # range 0–50

    # Choose symbol based on pulse polarity
    if pulse > 0:
        symbol = "█"
    elif pulse < 0:
        symbol = "▓"
    else:
        symbol = "░"

    bar = symbol * length

    print("\n=== WORLDHEART WAVEFORM ===")
    print(f"Pulse: {pulse:.2f}")
    print(bar)

    # Threshold markers
    if pulse >= 3.0:
        print(">> ASCENSION RHYTHM EMERGING <<")
    elif pulse <= -1.5:
        print(">> COLLAPSE RHYTHM EMERGING <<")
