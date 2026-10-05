import math

class PhaseOscillation:
    """
    Global cyclic rhythms for the BIG ANIMAL.
    Organs oscillate together in phase-locked breathing patterns.
    """

    def __init__(self):
        self.phase = 0.0          # global phase angle
        self.speed = 0.1          # base oscillation speed
        self.amplitude = 1.0      # oscillation strength
        self.mode = "neutral"     # current oscillation mode

    def update(self, state, synchrony, dt):
        """
        Update global phase and apply oscillatory effects.
        """

        # --- PHASE UPDATE ---
        # Synchrony increases oscillation speed
        self.speed = 0.1 + synchrony.coherence * 0.05

        # Advance phase
        self.phase += self.speed * dt

        # Keep phase in [0, 2π]
        if self.phase > math.tau:
            self.phase -= math.tau

        # --- MODE SELECTION ---
        if synchrony.coherence > 2.0:
            self.mode = "ascension_cycle"
        elif synchrony.coherence > 1.0:
            self.mode = "clarity_cycle"
        elif synchrony.coherence > 0.5:
            self.mode = "storm_cycle"
        else:
            self.mode = "collapse_cycle"

        # --- APPLY MODE ---
        if self.mode == "ascension_cycle":
            self.ascension_cycle(state, dt)
        elif self.mode == "clarity_cycle":
            self.clarity_cycle(state, dt)
        elif self.mode == "storm_cycle":
            self.storm_cycle(state, dt)
        else:
            self.collapse_cycle(state, dt)

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))

    # --- CYCLE MODES ---

    def ascension_cycle(self, state, dt):
        """
        World inhales clarity and exhales corruption.
        """
        wave = math.sin(self.phase) * self.amplitude * 0.02 * dt

        state["truth"] += wave
        state["pattern"] += wave
        state["balance"] += wave

        state["corruption"] -= wave * 0.8
        state["swarm"] -= wave * 0.8

    def clarity_cycle(self, state, dt):
        """
        World breathes cognitive clarity.
        """
        wave = math.sin(self.phase) * self.amplitude * 0.015 * dt

        state["truth"] += wave
        state["memory"] += wave
        state["pattern"] += wave

    def storm_cycle(self, state, dt):
        """
        World breathes emotional turbulence.
        """
        wave = math.sin(self.phase) * self.amplitude * 0.02 * dt

        state["decision"] += wave
        state["swarm"] += wave * 0.8
        state["corruption"] += wave * 0.6

    def collapse_cycle(self, state, dt):
        """
        World breathes collapse pressure.
        """
        wave = math.sin(self.phase) * self.amplitude * 0.01 * dt

        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] -= abs(wave)
