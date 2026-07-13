# mapper_core.py

from .reality_vector import build_reality_vector
from .recursive_compare import recursive_compare
from .refinement_engine import refine_models

class RealityMapper:
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
            "swarm": ...,
            "temporal": ...,
            "symbols": ...,
            "lattice": ...,
            "continuum": ...,
            "singularity": ...
        }
        """

        # 1. Build unified reality vector
        reality_vec = build_reality_vector(cognitive_inputs)

        # 2. Recursive comparison against internal models
        comparison = recursive_compare(reality_vec, cognitive_inputs)

        # 3. Refine cognitive models based on mismatch
        refinement = refine_models(comparison)

        # 4. Persist state
        self.state_store.save("reality_mapper_state", {
            "reality_vector": reality_vec.tolist(),
            "comparison": comparison,
            "refinement": refinement
        })

        return refinement
