def compute_physics(vectors, tensors):
    return {
        "energy": sum(vectors.values()),
        "flow": sum(tensors["attention"].values())
    }
