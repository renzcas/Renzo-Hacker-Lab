# recursive_compare.py

def recursive_compare(reality_vec, inputs):
    comparison = {}

    for key, organ in inputs.items():
        if "embedding" in organ:
            diff = reality_vec[:len(organ["embedding"])] - organ["embedding"]
            comparison[key] = float((diff**2).mean())

    return comparison
