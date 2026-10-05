class SwarmEngine:
    """
    Parasites, biomass, tunnels, mutation.
    Swarm grows by consuming nature and truth.
    """

    def update(self, state, dt: float):
        swarm = state["swarm"]

        # Feed on nature
        state["nature"] -= dt * (0.02 * swarm)

        # Feed on truth (misinformation)
        state["truth"] -= dt * (0.01 * swarm)

        # Swarm self-growth
        state["swarm"] += dt * (0.025 * swarm)
