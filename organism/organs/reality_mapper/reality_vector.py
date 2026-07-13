# reality_vector.py

import numpy as np

def build_reality_vector(inputs):
    vec = np.concatenate([
        inputs["intent"]["embedding"],
        inputs["future"]["embedding"],
        inputs["campaign"]["embedding"],
        inputs["defense"]["embedding"],
        inputs["healing"]["embedding"],
        inputs["swarm"]["embedding"],
        inputs["temporal"]["embedding"],
        inputs["symbols"]["embedding"],
        inputs["lattice"]["embedding"],
        inputs["continuum"]["embedding"],
        inputs["singularity"]["embedding"]
    ])
    return vec
