from organism.organism_state import initial_state
from organism.predator_prey_loop import organism_step
from simulation.endgame import EndgameController

# Engines (organs)
from engines.binary.binary_engine import BinaryEngine
from engines.techno.techno_engine import TechnoEngine
from engines.industrial.industrial_engine import IndustrialEngine
from engines.swarm.swarm_engine import SwarmEngine
from engines.truth.truth_engine import TruthEngine
from engines.archive.archive_engine import ArchiveEngine
from engines.pattern.pattern_engine import PatternEngine
from engines.balance.balance_engine import BalanceEngine
from engines.decision.decision_engine import DecisionEngine
from engines.worldheart.worldheart_engine import WorldheartEngine

# Events
from events.event_director import EventDirector

# Agents (neurons)
from agents.agent_manager import AgentManager
from agents.swarm_agents import RoachlingAgent, TunnelBrood
from agents.truth_agents import IntegrityKnight, AuroraScribe
from agents.balance_agents import HarmonyWarden, EquinoxGuardian
from agents.decision_agents import Stormcaller, BranchmindWeaver

# UI (face)
from ui.world_ui import WorldUI

# Worldheart subsystems (the full stack)
from worldheart.influence_matrix import InfluenceMatrix
from worldheart.feedback_loops import FeedbackLoops
from worldheart.entropy import OrganEntropy
from worldheart.recovery import OrganRecovery
from worldheart.shock import OrganShock
from worldheart.shielding import OrganShielding
from worldheart.overdrive import OrganOverdrive
from worldheart.synchrony import OrganSynchrony
from worldheart.phase_oscillation import PhaseOscillation
from worldheart.phase_coupling import PhaseCoupling
from worldheart.phase_turbulence import PhaseTurbulence
from worldheart.phase_collapse import PhaseCollapse
from worldheart.phase_rebirth import PhaseRebirth


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
        for engine in self.engines.values():
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
        self.phase_rebirth.update(self.state, self.phase_collapse, self.phase_coupling, dt)

        # 17. Event Director triggers mythic events
        events = self.event_director.update(self.state, dt)

        # 18. Agents react to events + state
        self.agents.update(self.state, events, dt)

        # 19. UI renders the organism
        self.ui.render(self.state, events)

        # 20. Endgame check
        end_event = self.endgame.check_endgame(self.state)
        if end_event:
            events.append(end_event)

        return self.state, events
