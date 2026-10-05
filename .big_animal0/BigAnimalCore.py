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

    def to_dict(self):
        return {
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
