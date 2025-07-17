import json
from game.ai.story_engine import generate_dynamic_story
from game.utils.game_state import save_state, load_state


def main():
    print("\n📜 Welcome back to Dungeons & LLMs!")

    # Load game state or create new one
    state = load_state()
    if not state:
        name = input("Enter your hero's name: ")
        player_class = input("Choose your class (e.g. Warrior, Mage, Rogue): ")
        state = {
            "player": {
                "name": name,
                "class": player_class,
                "hp": 100
            },
            "story": "",
            "last_action": "began their adventure"
        }
        print(f"🌟 A new journey begins for {name}, the {player_class}!")

    while True:
        # Get story narration and options from LLM
        story_text, options = generate_dynamic_story(state, state["last_action"])

        print("\n📖 Story:")
        print(story_text)

        print("\n🔮 Options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("0. Type your own action")

        choice = input("\n👉 What will you do? ")

        if choice == "0":
            action = input("Type your action: ")
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            action = options[int(choice) - 1]
        else:
            print("❗ Invalid input. Try again.")
            continue

        # Update state and loop
        state["last_action"] = action
        save_state(state)
        print("💾 Game state saved.")


if __name__ == "__main__":
    main()
