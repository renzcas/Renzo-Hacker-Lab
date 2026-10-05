class CaveBridge:
    """
    Bridge between the BIG ANIMAL kernel and the Cave# world.
    The kernel calls .send(event_type, payload) every tick.
    We simply store the last event so the cave can read it.
    """

    def __init__(self):
        # store last event sent to the cave
        self.last_event = None

    def send(self, event_type, payload):
        """
        Kernel calls this to send events to the cave.
        We store them so the cave engine (JS or C#) can read them.
        """
        self.last_event = {
            "type": event_type,
            "payload": payload
        }
        return self.last_event

    def translate(self, state):
        """
        Optional helper used by older versions of the engine.
        Converts pulse into a simple cave signal.
        """
        pulse = state.get("pulse", 0)

        if pulse >= 3.0:
            return {"signal": "ASCEND", "intensity": pulse}
        elif pulse <= -1.5:
            return {"signal": "COLLAPSE", "intensity": pulse}
        else:
            return {"signal": "STABLE", "intensity": pulse}
