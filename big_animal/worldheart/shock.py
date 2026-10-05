import random

class OrganShock:
    """
    Sudden destabilizing shocks to organs.
    Represents trauma, spikes, crashes, and acute world events.
    """

    def __init__(self):
        self.cooldown = 0.0

    def update(self, state, dt):
        """
        Apply shock events if cooldown allows.
        """

        # Reduce cooldown
        self.cooldown -= dt
        if self.cooldown > 0:
            return

        # Chance of shock increases with corruption + swarm + decision
        shock_pressure = (
            state["corruption"] +
            state["swarm"] +
            state["decision"]
        ) * 0.02

        # Random chance of shock
        if random.random() < shock_pressure:
            self.cooldown = 10.0  # prevent rapid shock spam
            self.apply_random_shock(state)

    def apply_random_shock(self, state):
        """
        Apply a random shock to one or more organs.
        """

        organs = [
            "truth", "memory", "balance", "pattern",
            "decision", "corruption", "swarm", "industrial"
        ]

        # Pick 1–3 organs to shock
        count = random.randint(1, 3)
        targets = random.sample(organs, count)

        for organ in targets:
            direction = random.choice(["spike", "crash"])

            if direction == "spike":
                magnitude = random.uniform(0.5, 2.0)
                state[organ] += magnitude
            else:
                magnitude = random.uniform(0.5, 2.0)
                state[organ] -= magnitude

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
