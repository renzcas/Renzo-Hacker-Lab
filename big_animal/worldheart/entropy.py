class OrganRecovery:
    """
    Healing, regeneration, and rebirth mechanics for organs.
    Counterbalances entropy and burnout.
    """

    def __init__(self):
        # Tracks regeneration momentum for each organ
        self.regen = {
            "truth": 0.0,
            "memory": 0.0,
            "balance": 0.0,
            "pattern": 0.0,
            "decision": 0.0,
            "corruption": 0.0,
            "swarm": 0.0,
            "industrial": 0.0,
        }

    def update(self, state, dt):
        """
        Apply regeneration and recovery effects.
        """

        # --- NATURAL REGENERATION ---
        for organ, value in state.items():
            if not isinstance(value, (int, float)):
                continue

            # Regeneration momentum increases when organ is low
            self.regen[organ] += (0.5 - abs(value)) * 0.01 * dt

            # Clamp regen
            self.regen[organ] = max(0.0, min(3.0, self.regen[organ]))

            # Apply regeneration
            state[organ] += self.regen[organ] * 0.004 * dt

        # --- GLOBAL RECOVERY WAVE ---
        # Triggered when truth + balance + pattern are high
        recovery_pressure = (
            state["truth"] +
            state["balance"] +
            state["pattern"]
        ) * 0.0004 * dt

        if recovery_pressure > 0.01:
            for organ in state:
                if isinstance(state[organ], (int, float)):
                    state[organ] += recovery_pressure

        # --- REBIRTH CYCLE ---
        # If collapse echo is high but pulse is rising,
        # the organism enters a rebirth cycle.
        if state["pulse"] > 0 and state["corruption"] < 1.0:
            for organ in state:
                if isinstance(state[organ], (int, float)):
                    state[organ] += 0.002 * dt  # gentle rebirth lift

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
