class OrganRecovery:
    """
    Healing, regeneration, and rebirth dynamics for organs.
    Counterbalances entropy and burnout.
    """

    def __init__(self):
        # Tracks healing momentum for each organ
        self.healing = {
            "truth": 0.0,
            "memory": 0.0,
            "balance": 0.0,
            "pattern": 0.0,
            "decision": 0.0,
            "corruption": 0.0,
            "swarm": 0.0,
            "industrial": 0.0,
        }

    def update(self, state, entropy, dt):
        """
        Apply healing and regeneration effects.
        """

        for organ, value in state.items():
            if not isinstance(value, (int, float)):
                continue

            # --- HEALING MOMENTUM ---
            # Healing increases when organ is low or entropy is high
            low_value_factor = max(0.0, (1.0 - abs(value) / 10.0))
            entropy_factor = entropy.burnout[organ] * 0.1

            self.healing[organ] += (low_value_factor + entropy_factor) * 0.01 * dt

            # Clamp healing momentum
            self.healing[organ] = max(0.0, min(5.0, self.healing[organ]))

            # --- APPLY HEALING ---
            # Healing momentum increases organ value
            state[organ] += self.healing[organ] * 0.004 * dt

        # --- GLOBAL REBIRTH SURGE ---
        # If truth + balance + pattern are high,
        # the entire organism receives a healing wave.
        rebirth_pressure = (
            state["truth"] +
            state["balance"] +
            state["pattern"]
        ) * 0.0004 * dt

        if rebirth_pressure > 0.01:
            for organ in state:
                if isinstance(state[organ], (int, float)):
                    state[organ] += rebirth_pressure

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
