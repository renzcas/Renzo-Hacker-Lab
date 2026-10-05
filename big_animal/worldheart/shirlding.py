class OrganShielding:
    """
    Protective buffers for organs.
    Reduces shock, entropy, burnout, and collapse pressure.
    """

    def __init__(self):
        # Each organ gets a shield layer
        self.shield = {
            "truth": 1.0,
            "memory": 1.0,
            "balance": 1.0,
            "pattern": 1.0,
            "decision": 1.0,
            "corruption": 1.0,
            "swarm": 1.0,
            "industrial": 1.0,
        }

        # Shield momentum (how quickly shields regenerate)
        self.momentum = {
            organ: 0.0 for organ in self.shield
        }

    def update(self, state, dt):
        """
        Apply shielding effects.
        """

        for organ, value in state.items():
            if not isinstance(value, (int, float)):
                continue

            # --- SHIELD MOMENTUM UPDATE ---
            # Shields regenerate faster when organ is stable
            stability_factor = max(0.0, 1.0 - abs(value) / 10.0)
            self.momentum[organ] += stability_factor * 0.01 * dt

            # Clamp momentum
            self.momentum[organ] = max(0.0, min(3.0, self.momentum[organ]))

            # --- SHIELD REGENERATION ---
            self.shield[organ] += self.momentum[organ] * 0.005 * dt

            # Clamp shield strength
            self.shield[organ] = max(0.0, min(5.0, self.shield[organ]))

            # --- APPLY SHIELDING ---
            # Shields reduce negative effects
            protection = self.shield[organ] * 0.02 * dt

            # Protect against entropy decay
            if value < 0:
                state[organ] += protection

            # Protect against shock crashes
            if value < -2.0:
                state[organ] += protection * 2.0

            # Protect against burnout
            if value < -1.0:
                state[organ] += protection * 1.5

        # --- GLOBAL SHIELD WAVE ---
        # If balance + truth are high, shields across the organism strengthen
        global_shield = (state["balance"] + state["truth"]) * 0.0005 * dt

        if global_shield > 0.01:
            for organ in self.shield:
                self.shield[organ] += global_shield

        # Clamp shield values
        for organ in self.shield:
            self.shield[organ] = max(0.0, min(5.0, self.shield[organ]))
