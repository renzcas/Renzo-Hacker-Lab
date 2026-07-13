# weave_core.py

from .weave_tensor import build_weave_tensor
from .weave_resolver import resolve_mission_paths
from .weave_projection import project_weave

class MissionWeave:
    def __init__(self, state_store):
        self.state_store = state_store

    def step(self, cognitive_inputs):
        """
        cognitive_inputs includes:
        - symbols (Φ)
        - lattice (∞)
        - continuum (Ω)
        - singularity (Z)
        - reality (Ψ)
        - mission (V)
        """

        weave_tensor = build_weave_tensor(cognitive_inputs)
        paths = resolve_mission_paths(weave_tensor, cognitive_inputs)
        projection = project_weave(paths)

        self.state_store.save("mission_weave_state", {
            "tensor": weave_tensor.tolist(),
            "paths": paths,
            "projection": projection
        })

        return projection
