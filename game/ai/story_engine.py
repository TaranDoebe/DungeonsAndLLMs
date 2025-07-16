import json
from DungeonsAndLLMs.game.ai.llm_generator import generate_monster


def generate_story_event(game_state):
    prompt = (
        "You are the narrator of an epic fantasy RPG.\n\n"
        f"The current game state is:\n{json.dumps(game_state, indent=2)}\n\n"
        "Generate a rich narrative scene describing what happens next. "
        "Make it immersive and dramatic. Include 2–3 player choices, each clearly labeled A), B), etc.\n\n"
        "Respond in plain text, not JSON."
    )
    return generate_monster(prompt)  # reuse your LLM call
