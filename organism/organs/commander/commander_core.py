# commander_core.py

from .command_vector import build_command_vector
from .command_physics import compute_command_physics
from .command_synthesis import synthesize_swarm_commands
from .swarm_protocol import execute_swarm_protocol

class Commander:
    def __init__(self, state_store):
        self.state_store = state_store

    def step(self, cognitive_inputs):
        """
        cognitive_inputs = {
            "intent": ...,
            "future": ...,
            "campaign": ...,
            "defense": ...,
            "healing": ...,
            "temporal": ...,
            "swarm": ...
        }
        """

        # 1. Build command vector
        cmd_vec = build_command_vector(cognitive_inputs)

        # 2. Physics-layer command dynamics
        physics = compute_command_physics(cmd_vec)

        # 3. LLM synthesis of swarm commands
        commands = synthesize_swarm_commands(cognitive_inputs, physics)

        # 4. Execute swarm protocol
        execute_swarm_protocol(commands)

        # 5. Persist commander state
        self.state_store.save("commander_state", {
            "command_vector": cmd_vec.tolist(),
            "physics": physics,
            "commands": commands
        })

        return commands
