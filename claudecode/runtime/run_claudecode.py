from claudecore.event_bus import bus
from claudecore.scanner import scan_repo
from claudecore.defender import defend

def run_claudecode():
    bus.subscribe("anomaly", defend)

    results = scan_repo()
    for a in results:
        bus.emit("anomaly", a)

if __name__ == "__main__":
    run_claudecode()
