class DecisionEngine:
    """
    Prefrontal cortex, emotional storms, narrative manipulation.
    Destabilizes balance and truth, increases corruption pressure.
    """

    def update(self, state, dt: float):
        dec = state["decision"]

        # Emotional storms weaken balance
        state["balance"] -= dt * (0.02 * dec)

        # Distort truth
        state["truth"] -= dt * (0.015 * dec)

        # Increase corruption (narrative fog)
        state["corruption"] += dt * (0.02 * dec)

