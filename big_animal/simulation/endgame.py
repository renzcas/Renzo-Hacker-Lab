class EndgameController:
    """
    Handles ascension and collapse sequences based on worldheart pulse
    and WW3 escalation. This is the fate engine of the BIG ANIMAL.
    """

    def __init__(self):
        self.ascended = False
        self.collapsed = False
        self.ascension_progress = 0.0
        self.collapse_progress = 0.0

    def update(self, state, events, dt):
        pulse = state["pulse"]
        ww3 = state["ww3_escalation"]

        # --- ASCENSION SEQUENCE ---
        if pulse >= 3.0 and not self.ascended:
            self.ascension_progress += dt * 0.1

            if self.ascension_progress >= 1.0:
                self.ascended = True
                events.append({"type": "ASCENSION_COMPLETE"})
                self._apply_ascension(state)

        # --- COLLAPSE SEQUENCE ---
        if pulse <= -1.5 and ww3 >= 2.0 and not self.collapsed:
            self.collapse_progress += dt * 0.1

            if self.collapse_progress >= 1.0:
                self.collapsed = True
                events.append({"type": "COLLAPSE_COMPLETE"})
                self._apply_collapse(state)

        return events

    def _apply_ascension(self, state):
        """
        Ascension transforms the organism into a high‑clarity state.
        """
        state["truth"] *= 2.0
        state["memory"] *= 1.5
        state["pattern"] *= 1.5
        state["balance"] *= 2.0

        state["swarm"] *= 0.2
        state["corruption"] *= 0.1
        state["industrial"] *= 0.5
        state["decision"] *= 0.3

        state["pulse"] = 5.0

    def _apply_collapse(self, state):
        """
        Collapse destroys the organism into entropy.
        """
        state["truth"] *= 0.1
        state["memory"] *= 0.2
        state["balance"] *= 0.1
        state["pattern"] *= 0.3

        state["swarm"] *= 3.0
        state["corruption"] *= 4.0
        state["industrial"] *= 2.0
        state["decision"] *= 3.0

        state["pulse"] = -5.0
