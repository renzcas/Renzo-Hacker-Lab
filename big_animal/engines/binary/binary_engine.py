class BinaryEngine:
    """
    Order, discipline, structure.
    Strengthens truth, reduces chaos, stabilizes prey.
    """

    def update(self, state, dt: float):
        order = state["binary"]

        # Strengthen truth
        state["truth"] += dt * (0.02 * order)

        # Reduce corruption slightly
        state["corruption"] -= dt * (0.01 * order)

        # Stabilize balance
        state["balance"] += dt * (0.015 * order)
