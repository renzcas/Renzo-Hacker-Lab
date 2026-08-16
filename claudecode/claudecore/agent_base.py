from claudecore.event_bus import bus

class ClaudeAgent:
    def __init__(self, name):
        self.name = name

    def on_event(self, event_type, handler):
        bus.subscribe(event_type, handler)

    def emit(self, event_type, payload):
        bus.emit(event_type, payload)
