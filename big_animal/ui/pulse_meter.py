# TODO: pulse meter rendering
def render_pulse_meter(pulse):
    """
    Displays the worldheart pulse.
    """
    print("\n=== WORLDHEART PULSE ===")
    print(f"Pulse: {pulse:.2f}")

    if pulse >= 3.0:
        print(">> ASCENSION THRESHOLD REACHED <<")
    elif pulse <= -1.5:
        print(">> COLLAPSE THRESHOLD <<")
