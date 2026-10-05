from agents.common_behaviors import clamp

class HarmonyWarden:
    """
    Stabilizes nature, truth, and emotional climate.
    """

    def update(self, state, events, dt):
        bal = state["balance"]

        # Stabilize nature
        state["nature"] += dt * (0.02 * bal)

        # Stabilize truth
        state["truth"] += dt * (0.015 * bal)

        # Reduce decision storms
        state["decision"] -= dt * (0.02 * bal)


class EquinoxGuardian:
    """
    Collapses chaos blooms during BALANCE events.
    """

    def update(self, state, events, dt):
        bal = state["balance"]

        if any(e["type"] == "BALANCE_BLOOM" for e in events):
            state["decision"] -= dt * (0.05 * bal)
            state["corruption"] -= dt * (0.03 * bal)

        # Passive calm
        state["balance"] += dt * (0.01 * bal)
