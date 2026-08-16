from claudecode.event_bus import bus

def attach_cockpit(cockpit):
    bus.subscribe("stimulus", lambda s: cockpit.record_event("stimulus", s))
    bus.subscribe("spike", lambda sp: cockpit.record_event("spike", sp))
    bus.subscribe("anomaly", lambda a: cockpit.record_event("anomaly", a))
    bus.subscribe("fuzz", lambda f: cockpit.record_event("fuzz", f))
    bus.subscribe("defense", lambda d: cockpit.record_event("defense", d))
