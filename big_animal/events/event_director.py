class WorldheartEngine:
    """
    The Worldheart is the central pulse generator of the BIG ANIMAL.
    It reads the global state and produces a single 'pulse' value that
    determines ascension, collapse, and world stability.
    """

    def compute_pulse(self, state):
        # Positive contributors (life)
        nature = state["nature"]
        truth = state["truth"]
        memory = state["memory"]
        balance = state["balance"]

        # Negative contributors (entropy)
        swarm = state["swarm"]
        corruption = state["corruption"]
        industrial = state["industrial"]
        decision = state["decision"]  # emotional storms

        # Vision + Order + Surveillance (meta‑stabilizers)
        pattern = state["pattern"]
        binary = state["binary"]
        techno = state["techno"]

        # --- LIFE FORCE ---
        life_force = (
            0.35 * nature +
            0.30 * truth +
            0.25 * memory +
            0.40 * balance +
            0.20 * pattern +
            0.15 * binary +
            0.10 * techno
        )

        # --- ENTROPY FORCE ---
        entropy_force = (
            0.40 * swarm +
            0.45 * corruption +
            0.35 * industrial +
            0.30 * decision
        )

        # --- RAW PULSE ---
        pulse = life_force - entropy_force

        # Clamp pulse to a reasonable range
        pulse = max(-5.0, min(5.0, pulse))

        return pulse

    def is_ascension_ready(self, pulse):
        """
        Ascension threshold: pulse must be high enough.
        """
        return pulse >= 3.0

    def is_collapse_imminent(self, pulse, ww3_escalation):
        """
        Collapse threshold: pulse low + WW3 high.
        """
        return pulse <= -1.5 and ww3_escalation >= 2.0

