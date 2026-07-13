# command_synthesis.py

def synthesize_swarm_commands(inputs, physics):
    return {
        "yara": ["boost-persistence", "enable-dll-sideloading"],
        "ioc": ["enrich-c2", "flag-credential-patterns"],
        "sandbox": ["prioritize-escalation", "monitor-lateral"],
        "swarm_phase": "phase-3-defensive-expansion",
        "confidence": physics["density"] / (physics["flow"] + 1e-6)
    }
