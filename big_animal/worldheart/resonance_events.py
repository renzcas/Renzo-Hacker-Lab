from ui.worldheart_harmonics import compute_harmonics

class ResonanceEvents:
    """
    Generates mythic events based on harmonic resonance patterns.
    LF = stability band
    MF = emotional band
    HF = cognitive band
    """

    def __init__(self):
        self.last_event_tick = 0

    def update(self, state, events, tick):
        pulse = state["pulse"]
        lf, mf, hf = compute_harmonics(pulse)

        # Prevent spam: only one resonance event every 10 ticks
        if tick - self.last_event_tick < 10:
            return events

        # --- ASCENSION RESONANCE ---
        if lf > 0.8 and mf < 0.3 and hf < 0.3:
            events.append({"type": "ASCENSION_RESONANCE"})
            self.last_event_tick = tick
            self._apply_ascension_resonance(state)
            return events

        # --- COLLAPSE RESONANCE ---
        if hf > 0.8 and mf > 0.7 and lf < 0.3:
            events.append({"type": "COLLAPSE_RESONANCE"})
            self.last_event_tick = tick
            self._apply_collapse_resonance(state)
            return events

        # --- EMOTIONAL SURGE ---
        if mf > 0.85 and hf < 0.5:
            events.append({"type": "EMOTIONAL_SURGE"})
            self.last_event_tick = tick
            state["decision"] += 0.3
            return events

        # --- COGNITIVE SPIKE ---
        if hf > 0.85 and mf < 0.5:
            events.append({"type": "COGNITIVE_SPIKE"})
            self.last_event_tick = tick
            state["pattern"] += 0.3
            return events

        # --- STABILITY BLOOM ---
        if lf > 0.9 and mf < 0.4 and hf < 0.4:
            events.append({"type": "STABILITY_BLOOM"})
            self.last_event_tick = tick
            state["balance"] += 0.4
            return events

        return events

    def _apply_ascension_resonance(self, state):
        state["truth"] += 0.5
        state["memory"] += 0.3
        state["balance"] += 0.4

    def _apply_collapse_resonance(self, state):
        state["corruption"] += 0.6
        state["swarm"] += 0.4
        state["decision"] += 0.5
