from __future__ import annotations
import math

class PhysicsDynamics:
    def __init__(self, damping: float = 0.99):
        self.damping = damping
        self.time_elapsed = 0.0

    def step(self, dt: float) -> float:
        self.time_elapsed += dt
        return self.time_elapsed * self.damping
