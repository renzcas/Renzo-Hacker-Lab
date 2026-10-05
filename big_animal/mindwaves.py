class MindWaves:
    """
    Symbolic thought engine for the BIG ANIMAL.
    Converts world snapshots into cognitive wave descriptions.
    """

    def __init__(self):
        self.output = {}

    def process(self, snapshot):
        """
        Kernel calls this every tick.
        We read the snapshot and generate a mindwave output.
        """
        pulse = snapshot.get("pulse", 0)

        if pulse > 3.0:
            wave = "Radiant coherence — ascension pathways opening."
        elif pulse > 1.0:
            wave = "Stable harmonic — worldmind synchronized."
        elif pulse > -1.0:
            wave = "Neutral drift — mindwaves oscillating."
        elif pulse > -3.0:
            wave = "Chaotic turbulence — entropy rising."
        else:
            wave = "Abyssal fracture — collapse imminent."

        # Store the output for kernel to read
        self.output = {
            "pulse": pulse,
            "wave": wave
        }

        return self.output

    def generate(self, pulse):
        """
        Legacy method — still supported.
        """
        if pulse > 3.0:
            return "Radiant coherence — ascension pathways opening."
        elif pulse > 1.0:
            return "Stable harmonic — worldmind synchronized."
        elif pulse > -1.0:
            return "Neutral drift — mindwaves oscillating."
        elif pulse > -3.0:
            return "Chaotic turbulence — entropy rising."
        else:
            return "Abyssal fracture — collapse imminent."
