import json
from DungeonsAndLLMs.game.ai.llm_generator import call_llm

def interpret_player_input(user_input, game_state):
    prompt = f"""
You are the game engine of a fantasy RPG.

The player just said: "{user_input}"

Here is the current game state:
{json.dumps(game_state, indent=2)}

Interpret their intent and respond with one of these commands only:
- fight
- rest
- info
- quit
- unknown

Respond only with the command, no explanation.
"""
    return call_llm(prompt).lower().strip()
