class OrganEntropy:
    """
    Tracks burnout and applies gradual entropy pressure to organ values.
    """

    def __init__(self):
        self.burnout = {
            organ: 0.0
            for organ in (
                "truth",
                "memory",
                "balance",
                "pattern",
                "decision",
                "corruption",
                "swarm",
                "industrial",
                "nature",
                "binary",
                "techno",
            )
        }

    def update(self, state, dt):
        for organ in self.burnout:
            value = state.get(organ)
            if not isinstance(value, (int, float)):
                continue

            load = max(0.0, abs(value) - 1.0)
            self.burnout[organ] = max(
                0.0,
                min(3.0, self.burnout[organ] + load * 0.001 * dt - 0.01 * dt),
            )
            state[organ] -= self.burnout[organ] * 0.003 * dt
