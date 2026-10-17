from __future__ import annotations
import math

def riemann_field(x: float) -> float:
    return math.tan(x) * 0.1 if abs(math.cos(x)) > 1e-5 else 0.0
