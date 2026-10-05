class FeedbackLoops:
    """
    Self-reinforcing organ feedback loops.
    Each organ has internal dynamics that amplify or dampen itself.
    """

    def __init__(self):
        # Internal momentum for each organ
        self.momentum = {
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
        Update organ momentum and apply feedback loops.
        """

        for organ, value in state.items():
            if not isinstance(value, (int, float)):
                continue

            # --- MOMENTUM UPDATE ---
            # Momentum increases when organ value is high
            # Momentum decreases when organ value is low
            self.momentum[organ] += (value * 0.01) * dt

            # Clamp momentum
            self.momentum[organ] = max(-5.0, min(5.0, self.momentum[organ]))

            # --- FEEDBACK LOOP ---
            # Positive momentum amplifies organ growth
            if self.momentum[organ] > 0:
                state[organ] += self.momentum[organ] * 0.005 * dt

            # Negative momentum dampens organ growth
            if self.momentum[organ] < 0:
                state[organ] += self.momentum[organ] * 0.003 * dt

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
