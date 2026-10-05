import random

class OrganOverdrive:
    """
    Temporary super-states for organs.
    Overdrive boosts organ values massively for short periods,
    followed by burnout and cooldown.
    """

    def __init__(self):
        self.cooldown = 0.0
        self.active = False
        self.duration = 0.0
        self.target_organs = []

    def update(self, state, dt):
        """
        Manage overdrive activation, duration, and cooldown.
        """

        # Reduce cooldown
        if self.cooldown > 0:
            self.cooldown -= dt

        # If overdrive is active, apply effects
        if self.active:
            self.apply_overdrive(state, dt)
            self.duration -= dt

            # End overdrive when duration expires
            if self.duration <= 0:
                self.end_overdrive(state)
            return

        # If cooldown is active, do nothing else
        if self.cooldown > 0:
            return

        # Chance of entering overdrive increases with:
        # - high truth + pattern (hyper-clarity)
        # - high decision (hyper-emotion)
        # - high industrial (hyper-production)
        # - high swarm (hyper-agitation)
        overdrive_pressure = (
            state["truth"] * 0.02 +
            state["pattern"] * 0.02 +
            state["decision"] * 0.03 +
            state["industrial"] * 0.03 +
            state["swarm"] * 0.03
        )

        if random.random() < overdrive_pressure:
            self.start_overdrive(state)

    def start_overdrive(self, state):
        """
        Activate overdrive for 1–3 organs.
        """

        self.active = True
        self.duration = random.uniform(5.0, 12.0)  # seconds of overdrive
        self.cooldown = random.uniform(15.0, 30.0)  # cooldown after overdrive

        organs = [
            "truth", "memory", "balance", "pattern",
            "decision", "corruption", "swarm", "industrial"
        ]

        # Pick 1–3 organs to supercharge
        count = random.randint(1, 3)
        self.target_organs = random.sample(organs, count)

        # Initial surge
        for organ in self.target_organs:
            state[organ] += random.uniform(1.0, 3.0)

    def apply_overdrive(self, state, dt):
        """
        Apply continuous overdrive effects.
        """

        for organ in self.target_organs:
            # Overdrive boosts organ value rapidly
            state[organ] += 0.2 * dt

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))

    def end_overdrive(self, state):
        """
        Apply burnout after overdrive ends.
        """

        self.active = False

        for organ in self.target_organs:
            # Burnout reduces organ value sharply
            state[organ] -= random.uniform(1.0, 2.5)

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
