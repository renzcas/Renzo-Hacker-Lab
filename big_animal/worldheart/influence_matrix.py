class InfluenceMatrix:
    """
    Defines how organs influence each other.
    This creates systemic, emergent behavior in the BIG ANIMAL.
    """

    def __init__(self):
        # Strength of influence between organs
        # These can be tuned later or even made dynamic
        self.matrix = {
            "truth": {
                "memory": +0.03,
                "pattern": +0.02,
                "corruption": -0.04,
                "decision": -0.02,
            },
            "memory": {
                "truth": +0.02,
                "pattern": +0.03,
                "balance": +0.02,
            },
            "balance": {
                "decision": -0.03,
                "swarm": -0.02,
                "corruption": -0.03,
            },
            "pattern": {
                "truth": +0.02,
                "decision": -0.02,
                "industrial": -0.01,
            },
            "decision": {
                "swarm": +0.03,
                "corruption": +0.04,
                "balance": -0.03,
            },
            "corruption": {
                "truth": -0.05,
                "memory": -0.03,
                "balance": -0.04,
            },
            "swarm": {
                "industrial": +0.03,
                "decision": +0.02,
            },
            "industrial": {
                "corruption": +0.03,
                "balance": -0.02,
            },
        }

    def update(self, state, dt):
        """
        Apply organ-to-organ influence.
        Each organ pushes or pulls other organs based on the matrix.
        """

        # Copy current organ values to avoid cascading within a single tick
        snapshot = {k: v for k, v in state.items() if isinstance(v, (int, float))}

        for organ, influences in self.matrix.items():
            source_value = snapshot.get(organ, 0.0)

            for target, strength in influences.items():
                if target in state:
                    state[target] += source_value * strength * dt

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
