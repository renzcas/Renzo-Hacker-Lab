class BigAnimalCore:
    """
    The central state container for the BIG ANIMAL.
    Holds all world parameters, life-force variables, entropy variables,
    and meta‑stabilizers.
    """

    def __init__(self):
        # --- LIFE FORCE ---
        self.nature = 1.0
        self.truth = 1.0
        self.memory = 1.0
        self.balance = 1.0

        # --- ENTROPY ---
        self.swarm = 0.5
        self.corruption = 0.5
        self.industrial = 0.5
        self.emotional_storm = 0.5

        # --- META-STABILIZERS ---
        self.pattern = 1.0
        self.binary = 1.0
        self.techno = 1.0

        # --- GLOBAL THREATS ---
        self.ww3_escalation = 0.0

        # --- INTERNAL STATE ---
        self.pulse = 0.0
        self.ascension_ready = False
        self.collapse_imminent = False

    # ---------------------------------------------------------
    # SNAPSHOT INPUT
    # ---------------------------------------------------------
    def pre_tick(self, snapshot):
        """
        Update core state values from the incoming snapshot.
        Any missing fields are ignored.
        """
        for key, value in snapshot.items():
            if hasattr(self, key):
                setattr(self, key, value)

    # ---------------------------------------------------------
    # WORLDHEART + STATE UPDATE
    # ---------------------------------------------------------
    def tick(self, snapshot):
        """
        Main world update step.
        Computes pulse and collapse/ascension flags.
        """

        # LIFE FORCE
        life_force = (
            0.35 * self.nature +
            0.30 * self.truth +
            0.25 * self.memory +
            0.40 * self.balance +
            0.20 * self.pattern +
            0.15 * self.binary +
            0.10 * self.techno
        )

        # ENTROPY FORCE
        entropy_force = (
            0.40 * self.swarm +
            0.45 * self.corruption +
            0.35 * self.industrial +
            0.30 * self.emotional_storm
        )

        # RAW PULSE
        pulse = life_force - entropy_force
        pulse = max(-5.0, min(5.0, pulse))
        self.pulse = pulse

        # ASCENSION / COLLAPSE
        self.ascension_ready = pulse >= 3.0
        self.collapse_imminent = pulse <= -1.5 and self.ww3_escalation >= 2.0

    # ---------------------------------------------------------
    # POST-TICK CLEANUP
    # ---------------------------------------------------------
    def post_tick(self, snapshot=None):
        """
        Placeholder for post-tick logic.
        """
        pass

    # ---------------------------------------------------------
    # SNAPSHOT OUTPUT
    # ---------------------------------------------------------
    def snapshot(self):
        """
        Return the full world state after tick.
        """
        return {
            "pulse": self.pulse,
            "ascension_ready": self.ascension_ready,
            "collapse_imminent": self.collapse_imminent,

            "nature": self.nature,
            "truth": self.truth,
            "memory": self.memory,
            "balance": self.balance,

            "swarm": self.swarm,
            "corruption": self.corruption,
            "industrial": self.industrial,
            "decision": self.emotional_storm,

            "pattern": self.pattern,
            "binary": self.binary,
            "techno": self.techno,

            "ww3_escalation": self.ww3_escalation
        }

    # ---------------------------------------------------------
    # RAW DICT EXPORT
    # ---------------------------------------------------------
    def to_dict(self):
        return self.snapshot()
