from agents.common_behaviors import clamp, move_toward, random_drift

class RoachlingAgent:
    """
    Basic swarm unit. Corrupts truth and nature.
    Moves toward corruption-rich states.
    """

    def update(self, state, events, dt):
        swarm = state["swarm"]

        # Drift toward corruption
        state["corruption"] = move_toward(state["corruption"], swarm * 0.8, dt * 0.02)

        # Corrupt nature
        state["nature"] -= dt * (0.01 * swarm)

        # Corrupt truth
        state["truth"] -= dt * (0.008 * swarm)

        # Random mutation drift
        state["swarm"] = clamp(random_drift(state["swarm"], 0.02))


class TunnelBrood:
    """
    Swarm tunneler. Expands corruption and swarm biomass.
    """

    def update(self, state, events, dt):
        swarm = state["swarm"]

        # Expand tunnels during SWARM_ECLIPSE
        if any(e["type"] == "SWARM_ECLIPSE" for e in events):
            state["swarm"] += dt * (0.05 * swarm)
            state["corruption"] += dt * (0.04 * swarm)

        # Normal tunneling
        state["corruption"] += dt * (0.02 * swarm)
        state["swarm"] += dt * (0.015 * swarm)
