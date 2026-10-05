from ui.worldheart_harmonics import compute_harmonics

class HarmonicMemory:
    """
    Stores long-term harmonic imprints from the worldheart.
    Harmonics accumulate over time and influence future pulse behavior.
    """

    def __init__(self):
        self.ascension_echo = 0.0
        self.collapse_echo = 0.0
        self.emotional_echo = 0.0
        self.cognitive_echo = 0.0
        self.stability_echo = 0.0

    def update(self, state, dt):
        pulse = state["pulse"]
        lf, mf, hf = compute_harmonics(pulse)

        # --- ACCUMULATE ECHOS ---
        self.stability_echo += lf * dt * 0.02
        self.emotional_echo += mf * dt * 0.02
        self.cognitive_echo += hf * dt * 0.02

        # Ascension echo: strong LF, weak MF/HF
        if lf > 0.8 and mf < 0.3 and hf < 0.3:
            self.ascension_echo += dt * 0.05

        # Collapse echo: strong HF, strong MF, weak LF
        if hf > 0.8 and mf > 0.7 and lf < 0.3:
            self.collapse_echo += dt * 0.05

        # --- APPLY MEMORY EFFECTS TO STATE ---
        # Stability echo calms corruption and decision storms
        state["corruption"] -= self.stability_echo * 0.01
        state["decision"] -= self.stability_echo * 0.01

        # Emotional echo increases decision storms
        state["decision"] += self.emotional_echo * 0.01

        # Cognitive echo increases pattern clarity
        state["pattern"] += self.cognitive_echo * 0.01

        # Ascension echo gently lifts pulse over time
        state["pulse"] += self.ascension_echo * 0.005

        # Collapse echo gently drags pulse downward
        state["pulse"] -= self.collapse_echo * 0.005

        # Clamp pulse to reasonable range
        state["pulse"] = max(-5.0, min(5.0, state["pulse"]))
