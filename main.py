import json
from game.ai.story_engine import generate_story_event
from game.engine.enemy import Enemy
from game.engine.player import Player
from game.engine.combat_manager import CombatManager
from game.utils.game_state import save_state, load_state
from game.ai.llm_generator import generate_monster, clean_llm_output

def main():
    state = load_state()
    player_data = state.get("player") or {
        "name": "Taran",
        "class": "Warrior",
        "hp": 100
    }
    player = Player(name=player_data["name"], player_class=player_data["class"])
    player.hp = player_data["hp"]

    print("\n📜 Welcome back to Dungeons & LLMs!")

    # Show story if we have one
    if state.get("last_action") == "combat_won":
        story = generate_story_event(state)
        print("\n📖 Your story continues...\n")
        print(story)

    while True:
        print("\n🌟 What would you like to do?")
        print("1. Continue your journey (fight new monster)")
        print("2. Rest and recover (+10 HP)")
        print("3. View player info")
        print("4. Quit game")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            # Generate and fight a new monster
            raw = generate_monster(
                "Create a level 1 fantasy monster. Respond in JSON format:\n"
                '{ "name": ..., "hp": ..., "attack_power": ..., "description": ... }'
            )
            print("🔍 Raw LLM output:\n", repr(raw))  # Add this line
            cleaned = clean_llm_output(raw)
            try:
                monster_data = json.loads(cleaned)
            except json.JSONDecodeError:
                print("❌ LLM output error, try again.")
                continue

            enemy = Enemy(
                name=monster_data["name"],
                hp=monster_data["hp"],
                attack_power=monster_data["attack_power"]
            )

            print(f"\n⚔️  You encounter a {enemy.name}!")
            print(f"📜  {monster_data['description']}\n")

            combat = CombatManager(player, enemy)
            combat.fight()

            state = {
                "player": {
                    "name": player.name,
                    "class": player.player_class,
                    "hp": player.hp
                },
                "enemy": {
                    "name": enemy.name,
                    "hp": enemy.hp,
                    "description": monster_data["description"]
                },
                "last_action": "combat_won" if enemy.hp <= 0 else "fled"
            }
            save_state(state)
            print("💾 Game state saved.")
            break  # return to menu on next run

        elif choice == "2":
            player.hp = min(player.hp + 10, 100)
            print(f"❤️ You rest and recover to {player.hp} HP.")
            state["player"] = {
                "name": player.name,
                "class": player.player_class,
                "hp": player.hp
            }
            state["last_action"] = "rested"
            save_state(state)

        elif choice == "3":
            print(f"\n👤 {player.name} the {player.player_class} | HP: {player.hp}")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❓ Invalid choice, try again.")

if __name__ == "__main__":
    main()
