# test_commander.py

from organism.runtime.dispatcher import Dispatcher

class DummyStore:
    def save(self, name, data):
        print(f"[STATE] {name} saved.")

def test_commander():
    dispatcher = Dispatcher(DummyStore())

    cognitive_inputs = {
        "intent": {"embedding": [0.1, 0.2, 0.3]},
        "future": {"embedding": [0.4, 0.5, 0.6]},
        "campaign": {"embedding": [0.7, 0.8, 0.9]},
        "defense": {"embedding": [1.0, 1.1, 1.2]},
        "healing": {"embedding": [1.3, 1.4, 1.5]},
        "temporal": {"embedding": [1.6, 1.7, 1.8]},
        "swarm": {"embedding": [1.9, 2.0, 2.1]}
    }

    dispatcher.tick(cognitive_inputs)
