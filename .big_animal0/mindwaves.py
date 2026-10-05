class MindWaves:
    def __init__(self):
        self.output = {}

    def process(self, snap):
        waves = {}

        waves["threat_wave"] = sum(
            t.get("aggression", 0) + t.get("chaos", 0)
            for t in snap["tribes"].values()
        )

        waves["opportunity_wave"] = sum(
            t.get("production", 0) + t.get("stability", 0)
            for t in snap["tribes"].values()
        )

        waves["corruption_wave"] = sum(
            len(v) for v in snap["corruption"].values()
        )

        waves["ascension_wave"] = sum(
            len(v) for v in snap["ascension"].values()
        )

        waves["era_pulse"] = hash(snap["era"]) % 1000

        self.output = waves
