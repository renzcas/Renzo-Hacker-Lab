from big_animal.organism.organism_state import initial_state
from big_animal.organism.predator_prey_loop import organism_step
from big_animal.simulation.endgame import EndgameController

# Engines (organs)
from big_animal.engines.binary.binary_engine import BinaryEngine
from big_animal.engines.techno.techno_engine import TechnoEngine
from big_animal.engines.industrial.industrial_engine import IndustrialEngine
from big_animal.engines.swarm.swarm_engine import SwarmEngine
from big_animal.engines.truth.truth_engine import TruthEngine
from big_animal.engines.archive.archive_engine import ArchiveEngine
from big_animal.engines.pattern.pattern_engine import PatternEngine
from big_animal.engines.balance.balance_engine import BalanceEngine
from big_animal.engines.decision.decision_engine import DecisionEngine
from big_animal.engines.worldheart.worldheart_engine import WorldheartEngine

# Events
from big_animal.events.event_director import EventDirector

# Agents (neurons)
from big_animal.agents.agent_manager import AgentManager
from big_animal.agents.swarm_agents import RoachlingAgent, TunnelBrood
from big_animal.agents.truth_agents import IntegrityKnight, AuroraScribe
from big_animal.agents.balance_agents import HarmonyWarden, EquinoxGuardian
from big_animal.agents.decision_agents import Stormcaller, BranchmindWeaver

# UI (face)
from big_animal.ui.world_ui import WorldUI

# Worldheart subsystems (the full stack)
from big_animal.worldheart.influence_matrix import InfluenceMatrix
from big_animal.worldheart.feedback_loops import FeedbackLoops
from big_animal.worldheart.entropy import OrganEntropy
from big_animal.worldheart.recovery import OrganRecovery
from big_animal.worldheart.shock import OrganShock
from big_animal.worldheart.shielding import OrganShielding
from big_animal.worldheart.overdrive import OrganOverdrive
from big_animal.worldheart.synchrony import OrganSynchrony
from big_animal.worldheart.phase_oscillation import PhaseOscillation
from big_animal.worldheart.phase_coupling import PhaseCoupling
from big_animal.worldheart.phase_turbulence import PhaseTurbulence
from big_animal.worldheart.phase_collapse import PhaseCollapse
from big_animal.worldheart.phase_rebirth import PhaseRebirth


class WorldOrganism:
    """
    The unified simulation organism.
    All engines, agents, events, and UI update through this loop.
    """

    def __init__(self):
        # Global state
        self.state = initial_state()

        # Engines (organs)
        self.engines = {
            "binary": BinaryEngine(),
            "techno": TechnoEngine(),
            "industrial": IndustrialEngine(),
            "swarm": SwarmEngine(),
            "truth": TruthEngine(),
            "archive": ArchiveEngine(),
            "pattern": PatternEngine(),
            "balance": BalanceEngine(),
            "decision": DecisionEngine(),
            "worldheart": WorldheartEngine(),
        }

        # Event brain
        self.event_director = EventDirector()

        # Agents (neurons)
        self.agents = AgentManager()
        self._spawn_default_agents()

        # UI (face)
        self.ui = WorldUI()

        # Endgame controller
        self.endgame = EndgameController()

        # Worldheart subsystems (the full stack)
        self.influence = InfluenceMatrix()
        self.feedback = FeedbackLoops()
        self.entropy = OrganEntropy()
        self.recovery = OrganRecovery()
        self.shock = OrganShock()
        self.shielding = OrganShielding()
        self.overdrive = OrganOverdrive()
        self.synchrony = OrganSynchrony()
        self.phase = PhaseOscillation()
        self.phase_coupling = PhaseCoupling()
        self.phase_turbulence = PhaseTurbulence()
        self.phase_collapse = PhaseCollapse()
        self.phase_rebirth = PhaseRebirth()


    def _spawn_default_agents(self):
        """
        Populate the organism with default agents.
        These act like neurons firing inside the world.
        """
        self.agents.add_agent(RoachlingAgent())
        self.agents.add_agent(TunnelBrood())

        self.agents.add_agent(IntegrityKnight())
        self.agents.add_agent(AuroraScribe())

        self.agents.add_agent(HarmonyWarden())
        self.agents.add_agent(EquinoxGuardian())

        self.agents.add_agent(Stormcaller())
        self.agents.add_agent(BranchmindWeaver())


    def step(self, dt: float):
        """
        One tick of the living organism.
        """

        # 1. Engines update the global state
        for name, engine in self.engines.items():
            if name != "worldheart":
                engine.update(self.state, dt)

        # 2. Predator–prey loop (heartbeat)
        self.state = organism_step(self.state, dt)

        # 3. Worldheart pulse
        pulse = self.engines["worldheart"].compute_pulse(self.state)
        self.state["pulse"] = pulse

        # 4. Influence Matrix (organ → organ influence)
        self.influence.update(self.state, dt)

        # 5. Feedback loops (self-reinforcement)
        self.feedback.update(self.state, dt)

        # 6. Entropy (decay, burnout)
        self.entropy.update(self.state, dt)

        # 7. Recovery (healing, regeneration)
        self.recovery.update(self.state, self.entropy, dt)

        # 8. Shock (trauma spikes)
        self.shock.update(self.state, dt)

        # 9. Shielding (protection, buffering)
        self.shielding.update(self.state, dt)

        # 10. Overdrive (temporary super-states)
        self.overdrive.update(self.state, dt)

        # 11. Synchrony (global alignment modes)
        self.synchrony.update(self.state, dt)

        # 12. Phase Oscillation (world-scale breathing)
        self.phase.update(self.state, self.synchrony, dt)

        # 13. Phase Coupling (organs influence each other's phases)
        self.phase_coupling.update(self.state, self.phase.phase, dt)

        # 14. Phase Turbulence (chaotic phase disruption)
        self.phase_turbulence.update(self.state, self.phase_coupling, dt)

        # 15. Phase Collapse (catastrophic rhythmic failure)
        self.phase_collapse.update(self.state, self.phase_coupling, self.phase_turbulence, dt)

        # 16. Phase Rebirth (post-collapse rhythmic reconstruction)
        self.phase_rebirth.update(self.state, self.phase_coupling, self.phase_collapse, dt)

        # 17. Event Director triggers mythic events
        events = self.event_director.update(self.state, dt)

        # 18. Agents react to events + state
        self.agents.update(self.state, events, dt)

        # 19. Endgame check
        events = self.endgame.update(self.state, events, dt)

        # 20. UI renders the organism
        self.ui.render(self.state, events)

        return self.state, events
