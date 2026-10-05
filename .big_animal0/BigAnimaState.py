class BigAnimalState:
    """
    Tracks the evolving condition of the BIG ANIMAL.
    Stores pulse, ascension, collapse, and world status.
    """

    def __init__(self):
        self.pulse = 0.0
        self.ascension_ready = False
        self.collapse_imminent = False

    def update(self, pulse, ascension_ready, collapse_imminent):
        self.pulse = pulse
        self.ascension_ready = ascension_ready
        self.collapse_imminent = collapse_imminent

    def to_dict(self):
        return {
            "pulse": self.pulse,
            "ascension_ready": self.ascension_ready,
            "collapse_imminent": self.collapse_imminent
        }
