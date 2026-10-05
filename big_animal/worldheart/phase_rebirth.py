import math
import random

class PhaseRebirth:
    """
    Reconstructs organ phases after catastrophic collapse.
    Restores rhythmic coherence and rebuilds oscillatory behavior.
    """

    def __init__(self):
        self.rebirth_level = 0.0
        self.active = False
        self.duration = 0.0

    def update(self, state, phase_coupling, phase_collapse, dt):
        """
        Manage rebirth activation, duration, and reconstruction.
        """

        # --- STEP 1: Increase rebirth pressure ---
        # Rebirth pressure increases when collapse pressure is high
        # but corruption and swarm begin to fall.
        self.rebirth_level += (
            phase_collapse.collapse_level * 0.05 -
            state["corruption"] * 0.02 -
            state["swarm"] * 0.02 +
            state["truth"] * 0.03 +
            state["balance"] * 0.03
        ) * dt

        # Clamp rebirth level
        self.rebirth_level = max(0.0, min(5.0, self.rebirth_level))

        # --- STEP 2: Trigger rebirth ---
        if not self.active and self.rebirth_level > 2.5:
            self.start_rebirth()

        # --- STEP 3: Apply rebirth effects ---
        if self.active:
            self.apply_rebirth(state, phase_coupling, dt)
            self.duration -= dt

            if self.duration <= 0:
                self.end_rebirth(state)

    def start_rebirth(self):
        """
        Activate rebirth for 6–18 seconds.
        """
        self.active = True
        self.duration = random.uniform(6.0, 18.0)

    def apply_rebirth(self, state, phase_coupling, dt):
        """
        Reconstruct organ phases and restore coherence.
        """

        for organ in phase_coupling.phases:
            # Phase healing: move phase toward global average
            avg_phase = sum(phase_coupling.phases.values()) / len(phase_coupling.phases)
            phase_coupling.phases[organ] += (avg_phase - phase_coupling.phases[organ]) * 0.05 * dt

            # Phase smoothing: reduce jagged turbulence
            phase_coupling.phases[organ] = (
                phase_coupling.phases[organ] * 0.9 +
                math.sin(phase_coupling.phases[organ]) * 0.1
            )

            # Phase stabilization: gently push toward rhythmic coherence
            phase_coupling.phases[organ] += math.sin(phase_coupling.phases[organ]) * 0.02 * dt

            # Wrap phase
            if phase_coupling.phases[organ] > math.tau:
                phase_coupling.phases[organ] -= math.tau
            if phase_coupling.phases[organ] < 0:
                phase_coupling.phases[organ] += math.tau

        # Apply rebirth to organ values
        for organ in state:
            if not isinstance(state[organ], (int, float)):
                continue

            # Rebirth gently lifts organ values
            state[organ] += 0.015 * dt * self.rebirth_level

            # Rebirth reduces corruption and swarm
            if organ in ["corruption", "swarm"]:
                state[organ] -= 0.02 * dt * self.rebirth_level

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))

    def end_rebirth(self, state):
        """
        Rebirth ends; rhythmic coherence restored.
        """
        self.active = False

        # Final coherence boost
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] += 0.02

        # Reduce rebirth pressure
        self.rebirth_level *= 0.4
