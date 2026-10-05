class IndustrialEngine:
    """
    Metabolism, machinery, smog, pipelines.
    Increases industrial pressure and corruption baseline.
    """

    def update(self, state, dt: float):
        ind = state["industrial"]

        # Industrial growth
        state["industrial"] += dt * (0.03 * ind)

        # Pollution → corruption
        state["corruption"] += dt * (0.02 * ind)

        # Nature damage
        state["nature"] -= dt * (0.015 * ind)
