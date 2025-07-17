from DungeonsAndLLMs.game.utils.game_state import load_state, save_state
from DungeonsAndLLMs.game.ai.llm_generator import generate_story_text

def build_story_prompt(state):
    player = state.get("player", {})
    story = state.setdefault("story", {})

    history = story.get("history", [])
    location = story.get("location", "Unknown")
    quest = story.get("current_quest", "None")
    last_event = story.get("last_event", "")

    history_str = "\n".join(history[-5:]) if history else "None yet."

    return (
        f"You are a fantasy RPG narrator.\n"
        f"Player: {player.get('name', 'Hero')} ({player.get('class', 'Adventurer')})\n"
        f"Location: {location}\n"
        f"Current Quest: {quest}\n"
        f"Recent Events:\n{history_str}\n\n"
        f"Write the next scene in 2–3 sentences and then present 2 numbered choices for what the player can do next."
    )


def advance_story():
    state = load_state()
    prompt = build_story_prompt(state)

    print("\n🧠 Generating next story scene...")
    output = generate_story_text(prompt)
    print("\n📜 Story:")
    print(output)

    # Save the story output and prompt for later use
    story = state.setdefault("story", {})
    story["last_scene"] = output
    story.setdefault("history", []).append(output)
    save_state(state)