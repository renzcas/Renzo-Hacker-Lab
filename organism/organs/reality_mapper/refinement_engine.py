# refinement_engine.py

def refine_models(comparison):
    refined = {}

    for organ, mismatch in comparison.items():
        refined[organ] = {
            "adjustment": mismatch * 0.01,
            "status": "refined" if mismatch > 0.1 else "stable"
        }

    return refined
