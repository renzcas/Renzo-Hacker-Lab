class UTEState:
    def __init__(self):
        self.embeddings = {}
        self.vectors = {}
        self.tensors = {}
        self.physics = {}

    def sync(self, new_state):
        self.embeddings = new_state.get("embeddings", {})
        self.vectors = new_state.get("vectors", {})
        self.tensors = new_state.get("tensors", {})
        self.physics = new_state.get("physics", {})
