from ute.core.state import UTEState
from ute.math.vectors import build_vectors
from ute.math.embeddings import build_embeddings
from ute.math.tensors import build_tensors
from ute.math.physics import compute_physics

class UnifiedTheoryEngine:
    def __init__(self):
        self.state = UTEState()

    def update(self, inputs):
        """
        inputs = {
            "stimulus": {...},
            "spikes": [...],
            "anomalies": [...],
            "defense": [...]
        }
        """

        embeddings = build_embeddings(inputs)
        vectors = build_vectors(inputs)
        tensors = build_tensors(inputs, vectors)
        physics = compute_physics(vectors, tensors)

        self.state.sync({
            "embeddings": embeddings,
            "vectors": vectors,
            "tensors": tensors,
            "physics": physics
        })

        return self.state
