class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, handler):
        self.subscribers.setdefault(event_type, []).append(handler)

    def emit(self, event_type, payload):
        for handler in self.subscribers.get(event_type, []):
            handler(payload)

bus = EventBus()
