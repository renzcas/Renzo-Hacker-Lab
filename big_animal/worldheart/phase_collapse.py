import math
import random

class PhaseCollapse:
    """
    Catastrophic rhythmic failure.
    Total desynchronization of organ phases.
    """

    def __init__(self):
        self.collapse_level = 0.0
        self.active = False
        self.duration = 0.0

    def update(self, state, phase_coupling, turbulence, dt):
        """
        Manage collapse activation, duration, and recovery.
        """

        # --- STEP 1: Increase collapse pressure ---
        self.collapse_level += (
            turbulence.intensity * 0.05 +
            state["corruption"] * 0.03 +
            state["swarm"] * 0.02 +
            state["decision"] * 0.02 -
            state["balance"] * 0.04
        ) * dt

        # Clamp collapse level
        self.collapse_level = max(0.0, min(5.0, self.collapse_level))

        # --- STEP 2: Trigger collapse ---
        if not self.active and self.collapse_level > 3.0:
            self.start_collapse()

        # --- STEP 3: If collapse is active, apply effects ---
        if self.active:
            self.apply_collapse(state, phase_coupling, dt)
            self.duration -= dt

            if self.duration <= 0:
                self.end_collapse(state)

    def start_collapse(self):
        """
        Activate collapse for 5–15 seconds.
        """
        self.active = True
        self.duration = random.uniform(5.0, 15.0)

    def apply_collapse(self, state, phase_coupling, dt):
        """
        Apply catastrophic phase failure.
        """

        for organ in phase_coupling.phases:
            # Phase shattering: randomize phase
            phase_coupling.phases[organ] = random.random() * math.tau

            # Phase freeze: occasionally lock phase
            if random.random() < 0.1:
                phase_coupling.phases[organ] = 0.0

            # Phase inversion storm
            if random.random() < 0.05:
                phase_coupling.phases[organ] = math.pi - phase_coupling.phases[organ]

        # Apply collapse to organ values
        for organ in state:
            if not isinstance(state[organ], (int, float)):
                continue

            # Collapse drains organ values
            state[organ] -= 0.02 * dt * self.collapse_level

            # Collapse spikes corruption and swarm
            if organ in ["corruption", "swarm"]:
                state[organ] += 0.03 * dt * self.collapse_level

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))

    def end_collapse(self, state):
        """
        Collapse ends; recovery inertia begins.
        """
        self.active = False

        # Collapse recovery inertia: slow rebound
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] += 0.01  # gentle lift

        # Reduce collapse pressure
        self.collapse_level *= 0.5
