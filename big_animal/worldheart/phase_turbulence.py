import math
import random

class PhaseTurbulence:
    """
    Chaotic disruption of organ phases.
    Introduces nonlinear oscillation storms and phase divergence.
    """

    def __init__(self):
        self.intensity = 0.0  # global turbulence level

    def update(self, state, phase_coupling, dt):
        """
        Apply turbulence to organ phases.
        """

        # --- STEP 1: Turbulence intensity calculation ---
        # Turbulence increases with:
        # - high corruption
        # - high swarm
        # - high decision storms
        # - low balance
        self.intensity += (
            state["corruption"] * 0.02 +
            state["swarm"] * 0.015 +
            state["decision"] * 0.01 -
            state["balance"] * 0.02
        ) * dt

        # Clamp intensity
        self.intensity = max(0.0, min(3.0, self.intensity))

        # --- STEP 2: Apply turbulence to phases ---
        for organ in phase_coupling.phases:
            # Random noise injection
            noise = (random.random() - 0.5) * self.intensity * 0.1 * dt
            phase_coupling.phases[organ] += noise

            # Nonlinear phase distortion
            distortion = math.sin(phase_coupling.phases[organ] * 3.0) * self.intensity * 0.05 * dt
            phase_coupling.phases[organ] += distortion

            # Phase inversion (rare)
            if self.intensity > 2.5 and random.random() < 0.01:
                phase_coupling.phases[organ] = math.pi - phase_coupling.phases[organ]

            # Wrap phase
            if phase_coupling.phases[organ] > math.tau:
                phase_coupling.phases[organ] -= math.tau
            if phase_coupling.phases[organ] < 0:
                phase_coupling.phases[organ] += math.tau

        # --- STEP 3: Apply turbulence to organ values ---
        for organ in state:
            if not isinstance(state[organ], (int, float)):
                continue

            # Turbulence causes chaotic oscillation
            chaotic_wave = math.sin(phase_coupling.phases.get(organ, 0.0) * 2.0) * self.intensity * 0.01 * dt
            state[organ] += chaotic_wave

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
