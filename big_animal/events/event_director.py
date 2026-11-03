from big_animal.events.resonance_events import ResonanceEvents


class EventDirector:
    def __init__(self):
        self.tick_count = 0
        self.resonance_events = ResonanceEvents()

    def update(self, state, dt):
        self.tick_count += 1
        return self.resonance_events.update(state, [], self.tick_count)

