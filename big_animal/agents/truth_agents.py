from agents.common_behaviors import clamp, move_toward

class IntegrityKnight:
    """
    Purifies corruption, strengthens truth.
    Moves toward corruption hotspots.
    """

    def update(self, state, events, dt):
        truth = state["truth"]

        # Move toward corruption
        state["corruption"] = move_toward(state["corruption"], 0.0, dt * 0.03)

        # Purify corruptions
        state["corruption"] -= dt * (0.03 * truth)

        # Strengthen truth
        state["truth"] += dt * (0.02 * truth)

        # Memory synergy
        state["memory"] += dt * (0.01 * truth)


class AuroraScribe:
    """
    Truth archivist. Boosts memory and truth during CRYSTAL_DAWN.
    """

    def update(self, state, events, dt):
        truth = state["truth"]

        if any(e["type"] == "CRYSTAL_DAWN" for e in events):
            state["truth"] += dt * (0.05 * truth)
            state["memory"] += dt * (0.04 * truth)

        # Passive clarity
        state["pattern"] += dt * (0.01 * truth)
