from __future__ import annotations
import math

def entropy(x: float) -> float:
    return math.log(abs(x) + 1) * 0.7
