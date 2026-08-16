from ute.core.engine import UnifiedTheoryEngine

def run_ute_cycle(inputs):
    ute = UnifiedTheoryEngine()
    return ute.update(inputs)
