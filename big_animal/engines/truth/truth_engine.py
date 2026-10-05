class TruthEngine:
    """
    Purification, integrity, merkle storms.
    Reduces corruption and strengthens memory.
    """

    def update(self, state, dt: float):
        truth = state["truth"]

        # Purify corruption
        state["corruption"] -= dt * (0.03 * truth)

        # Strengthen memory
        state["memory"] += dt * (0.02 * truth)

        # Slightly weaken swarm (clarity)
        state["swarm"] -= dt * (0.01 * truth)
