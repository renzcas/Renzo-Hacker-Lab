import math


def compute_harmonics(pulse):
    pulse = max(-5.0, min(5.0, pulse))
    return (
        math.sin(pulse * 0.4) * 0.5 + 0.5,
        math.sin(pulse * 1.2) * 0.5 + 0.5,
        math.sin(pulse * 3.5) * 0.5 + 0.5,
    )