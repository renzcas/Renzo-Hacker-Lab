from ui.worldheart_harmonics import compute_harmonics

class WorldheartDrift:
    """
    Slow global evolution of organ weights based on harmonic memory.
    This is the ecological drift of the BIG ANIMAL.
    """

    def __init__(self):
        self.ascension_bias = 0.0
        self.collapse_bias = 0.0

    def update(self, state, harmonic_memory, dt):
        pulse = state["pulse"]
        lf, mf, hf = compute_harmonics(pulse)

        # --- UPDATE BIASES FROM HARMONIC MEMORY ---
        self.ascension_bias += harmonic_memory.ascension_echo * dt * 0.01
        self.collapse_bias += harmonic_memory.collapse_echo * dt * 0.01

        # Clamp biases
        self.ascension_bias = min(self.ascension_bias, 3.0)
        self.collapse_bias = min(self.collapse_bias, 3.0)

        # --- APPLY GLOBAL DRIFT ---
        # Ascension drift pushes clarity organs upward
        state["truth"] += self.ascension_bias * 0.002
        state["memory"] += self.ascension_bias * 0.002
        state["balance"] += self.ascension_bias * 0.002
        state["pattern"] += self.ascension_bias * 0.002

        # Collapse drift pushes entropy organs upward
        state["corruption"] += self.collapse_bias * 0.003
        state["swarm"] += self.collapse_bias * 0.002
        state["industrial"] += self.collapse_bias * 0.002
        state["decision"] += self.collapse_bias * 0.003

        # Harmonic-driven drift
        # LF → stability organs
        state["balance"] += lf * dt * 0.001

        # MF → emotional organs
        state["decision"] += mf * dt * 0.001

        # HF → cognitive organs
        state["pattern"] += hf * dt * 0.001

        # Clamp organ values to reasonable ranges
        for organ in state:
            if isinstance(state[organ], (int, float)):
                state[organ] = max(-10.0, min(10.0, state[organ]))
