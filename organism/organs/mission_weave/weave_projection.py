# weave_projection.py

def project_weave(paths):
    return [
        {"task": paths["primary"], "priority": 1},
        {"task": paths["secondary"], "priority": 2},
        {"task": paths["tertiary"], "priority": 3}
    ]
