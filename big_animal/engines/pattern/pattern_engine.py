class PatternEngine:
    """
    Vision cortex, detection, scanning, future echoes.
    Reveals predators and weakens swarm/corruption.
    """

    def update(self, state, dt: float):
        pat = state["pattern"]

        # Reveal swarm tunnels
        state["swarm"] -= dt * (0.02 * pat)

        # Reveal corruption pockets
        state["corruption"] -= dt * (0.015 * pat)

        # Boost truth clarity
        state["truth"] += dt * (0.01 * pat)
