from ui.worldheart_harmonics import compute_harmonics

class OrganSynchrony:
    """
    Aligns organs into unified modes based on harmonic coherence.
    Creates global states: clarity, storm, collapse, ascension.
    """

    def __init__(self):
        self.coherence = 0.0  # global synchrony level

    def update(self, state, dt):
        pulse = state["pulse"]
        lf, mf, hf = compute_harmonics(pulse)

        # --- COHERENCE CALCULATION ---
        # Coherence increases when harmonics align
        harmonic_alignment = (
            abs(lf - mf) +
            abs(mf - hf) +
            abs(hf - lf)
        )

        # Lower alignment difference → higher coherence
        self.coherence += (1.5 - harmonic_alignment) * 0.01 * dt

        # Clamp coherence
        self.coherence = max(0.0, min(3.0, self.coherence))

        # --- APPLY SYNCHRONY MODES ---
        if self.coherence > 2.0:
            self.ascension_mode(state, dt)
        elif self.coherence > 1.0:
            self.clarity_mode(state, dt)
        elif self.coherence > 0.5:
            self.storm_mode(state, dt)
        else:
            self.collapse_mode(state, dt)

        # Clamp organ values
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))

    # --- SYNCHRONY MODES ---

    def clarity_mode(self, state, dt):
        """
        Organs align into a clarity state.
        Truth, memory, pattern rise together.
        """
        state["truth"] += 0.01 * dt
        state["memory"] += 0.01 * dt
        state["pattern"] += 0.01 * dt

    def storm_mode(self, state, dt):
        """
        Organs align into an emotional storm.
        Decision, swarm, corruption rise together.
        """
        state["decision"] += 0.015 * dt
        state["swarm"] += 0.01 * dt
        state["corruption"] += 0.01 * dt

    def collapse_mode(self, state, dt):
        """
        Organs align into a collapse drift.
        Everything decays slightly.
        """
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] -= 0.005 * dt

    def ascension_mode(self, state, dt):
        """
        Organs align into ascension.
        Truth, balance, pattern rise together.
        Corruption and swarm fall.
        """
        state["truth"] += 0.02 * dt
        state["balance"] += 0.02 * dt
        state["pattern"] += 0.02 * dt

        state["corruption"] -= 0.015 * dt
        state["swarm"] -= 0.015 * dt
