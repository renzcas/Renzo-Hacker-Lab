# TODO: tick utilities
class Tick:
    """
    Simple tick controller for the BIG ANIMAL.
    Tracks time delta, tick count, and provides helpers
    for cooldowns and tick-based scaling.
    """

    def __init__(self, dt=1.0):
        self.dt = dt
        self.count = 0

    def step(self):
        """
        Advance one tick and return dt.
        """
        self.count += 1
        return self.dt

    def every(self, n):
        """
        Returns True every n ticks.
        Useful for periodic events or logging.
        """
        return self.count % n == 0

    def cooldown(self, timer, rate=1.0):
        """
        Reduces a cooldown timer by dt * rate.
        Returns the updated timer.
        """
        timer -= self.dt * rate
        if timer < 0:
            timer = 0
        return timer
