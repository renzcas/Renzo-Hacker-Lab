# weave_tensor.py

import numpy as np

def build_weave_tensor(inputs):
    vec = np.concatenate([
        inputs["symbols"]["embedding"],
        inputs["lattice"]["embedding"],
        inputs["continuum"]["embedding"],
        inputs["singularity"]["embedding"],
        inputs["reality"]["embedding"],
        inputs["mission"]["embedding"]
    ])
    return vec
