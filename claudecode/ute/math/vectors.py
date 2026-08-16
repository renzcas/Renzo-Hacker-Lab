def build_vectors(inputs):
    return {
        "stimulus_vec": len(str(inputs.get("stimulus", ""))),
        "spike_vec": len(inputs.get("spikes", [])),
        "anomaly_vec": len(inputs.get("anomalies", [])),
        "defense_vec": len(inputs.get("defense", []))
    }
