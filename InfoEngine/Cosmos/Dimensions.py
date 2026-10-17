from __future__ import annotations
import math

class Dimensions:
    def __init__(self, space_dim: int = 3, time_dim: int = 1):
        self.space_dim = space_dim
        self.time_dim = time_dim

    def distance(self, p1, p2) -> float:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

    def norm(self, vec) -> float:
        return math.sqrt(sum(v * v for v in vec))

    def energy_scale(self, mass: float, velocity: float) -> float:
        return 0.5 * mass * velocity * velocity

    def normalize_field(self, field):
        if not field:
            return []
        mn = min(field)
        mx = max(field)
        return [(v - mn) / (mx - mn) if mx != mn else 0.0 for v in field]
