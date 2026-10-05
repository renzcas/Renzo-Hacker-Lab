# TODO: event log rendering
def render_event_log(events):
    """
    Prints events triggered this tick.
    """
    print("\n=== EVENT LOG ===")
    if not events:
        print("No events this tick.")
        return

    for e in events:
        print(f"Event: {e['type']}")
