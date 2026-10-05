from ui.organ_wheel import render_organ_wheel
from ui.climate_strip import render_climate_strip
from ui.pulse_meter import render_pulse_meter
from ui.event_log import render_event_log

class WorldUI:
    """
    The UI layer of the BIG ANIMAL.
    For now, this prints simple text summaries.
    Later you can replace these with real graphics.
    """

    def render(self, state, events):
        # Pulse bar
        render_pulse_meter(state["pulse"])

        # Organ wheel
        render_organ_wheel(state)

        # Climate strip
        render_climate_strip(state)

        # Event log
        render_event_log(events)
