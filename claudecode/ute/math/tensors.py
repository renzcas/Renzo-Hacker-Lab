def build_tensors(inputs, vectors):
    return {
        "attention": {
            "stimulus": vectors["stimulus_vec"] * 0.1,
            "spike": vectors["spike_vec"] * 0.2,
            "anomaly": vectors["anomaly_vec"] * 0.3,
            "defense": vectors["defense_vec"] * 0.4
        }
    }
