import math

class PhaseCoupling:
    """
    Organs influence each other's oscillation phases.
    Creates internal rhythmic intelligence and phase-locked behavior.
    """

    def __init__(self):
        # Each organ has its own phase angle
        self.phases = {
            "truth": 0.0,
            "memory": 0.0,
            "balance": 0.0,
            "pattern": 0.0,
            "decision": 0.0,
            "corruption": 0.0,
            "swarm": 0.0,
            "industrial": 0.0,
        }

        # Coupling strength between organs
        self.coupling_strength = 0.05

    def update(self, state, global_phase, dt):
        """
        Update organ phases based on global phase and organ interactions.
        """

        # --- STEP 1: Advance each organ's phase ---
        for organ in self.phases:
            # Base oscillation speed influenced by organ value
            speed = 0.1 + abs(state[organ]) * 0.01
            self.phases[organ] += speed * dt

            # Wrap phase
            if self.phases[organ] > math.tau:
                self.phases[organ] -= math.tau

        # --- STEP 2: Phase coupling between organs ---
        organs = list(self.phases.keys())

        for i in range(len(organs)):
            for j in range(i + 1, len(organs)):
                a = organs[i]
                b = organs[j]

                # Phase difference
                diff = self.phases[a] - self.phases[b]

                # Coupling force (Kuramoto-style)
                force = math.sin(diff) * self.coupling_strength * dt

                # Strong organs impose their phase more
                strength_a = abs(state[a]) + 1.0
                strength_b = abs(state[b]) + 1.0

                # Apply coupling
                self.phases[a] -= force * (strength_b / (strength_a + strength_b))
                self.phases[b] += force * (strength_a / (strength_a + strength_b))

        # --- STEP 3: Apply phase influence to organ values ---
        for organ in self.phases:
            wave = math.sin(self.phases[organ]) * 0.01 * dt
            state[organ] += wave

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
