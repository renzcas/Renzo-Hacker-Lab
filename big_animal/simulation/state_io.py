import json

class StateIO:
    """
    Handles saving and loading the BIG ANIMAL world state.
    Uses JSON for portability and readability.
    """

    def save(self, state, path="world_state.json"):
        """
        Saves the entire organism state to a JSON file.
        """
        with open(path, "w") as f:
            json.dump(state, f, indent=4)
        print(f"[STATE SAVED] → {path}")

    def load(self, path="world_state.json"):
        """
        Loads a world state from a JSON file.
        Returns the state dict.
        """
        with open(path, "r") as f:
            state = json.load(f)
        print(f"[STATE LOADED] ← {path}")
        return state
