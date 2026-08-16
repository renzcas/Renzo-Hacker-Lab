from claudecore.agent_base import ClaudeAgent
from claudecore.event_bus import bus

class BinaryCommandAgent(ClaudeAgent):
    def __init__(self):
        super().__init__("BinaryCommandAgent")

    def fuzz(self, anomalies):
        """
        Minimal fuzzing:
        - amplify anomaly scores
        - generate fuzz events
        """
        fuzz_events = []
        for a in anomalies:
            amplified = {
                "path": a["path"],
                "fuzzScore": a["score"] * 1.5,
                "entropy": a["entropy"],
                "weird": a["weird"]
            }
            fuzz_events.append(amplified)
            bus.emit("fuzz", amplified)
        return fuzz_events

    def generate_defense(self, fuzz_events):
        """
        Minimal defense signal:
        - if fuzzScore is high, emit defense event
        """
        defense_signals = []
        for f in fuzz_events:
            if f["fuzzScore"] > 15:
                signal = {
                    "action": "block",
                    "target": f["path"],
                    "reason": "high fuzzScore",
                    "score": f["fuzzScore"]
                }
                defense_signals.append(signal)
                bus.emit("defense", signal)
        return defense_signals

    def run(self, anomalies):
        fuzz_events = self.fuzz(anomalies)
        defense_signals = self.generate_defense(fuzz_events)
        return fuzz_events, defense_signals
