def build_embeddings(inputs):
    return {
        "stimulus": inputs.get("stimulus"),
        "spikes": inputs.get("spikes"),
        "anomalies": inputs.get("anomalies"),
        "defense": inputs.get("defense")
    }
