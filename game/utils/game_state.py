import json
import os

STATE_PATH = "DungeonsAndLLMs/data/game_state.json"

def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def load_state():
    if not os.path.exists(STATE_PATH):
        return {}
    with open(STATE_PATH, "r") as f:
        return json.load(f)

def reset_state():
    if os.path.exists(STATE_PATH):
        os.remove(STATE_PATH)
