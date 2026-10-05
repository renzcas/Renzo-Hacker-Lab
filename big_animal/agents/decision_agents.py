from agents.common_behaviors import random_drift

class Stormcaller:
    """
    Generates emotional storms, destabilizes truth and balance.
    """

    def update(self, state, events, dt):
        dec = state["decision"]

        # Emotional storms
        state["balance"] -= dt * (0.03 * dec)
        state["truth"] -= dt * (0.02 * dec)

        # Increase corruption
        state["corruption"] += dt * (0.025 * dec)

        # Random emotional drift
        state["decision"] = random_drift(state["decision"], 0.03)


class BranchmindWeaver:
    """
    Narrative manipulator. Amplifies chaos during COLLAPSE_START.
    """

    def update(self, state, events, dt):
        dec = state["decision"]

        if any(e["type"] == "COLLAPSE_START" for e in events):
            state["truth"] -= dt * (0.04 * dec)
            state["balance"] -= dt * (0.05 * dec)
            state["corruption"] += dt * (0.05 * dec)

        # Passive manipulation
        state["decision"] += dt * (0.01 * dec)
