from game.engine.player import Player
from game.engine.enemy import Enemy
from game.engine.combat_manager import CombatManager


def main():
    print("=== Welcome to Dungeons & LLMs ===")
    name = input("Enter your name: ")
    print("Choose your class:")
    print("1. Warrior (High damage, high defense)")
    print("2. Rogue (Lower damage, faster turns later?)")
    class_choice = input("Enter 1 or 2: ")

    if class_choice == "1":
        player_class = "Warrior"
    elif class_choice == "2":
        player_class = "Rogue"
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player_class = "Warrior"

    player = Player(name=name, player_class=player_class)
    enemy = Enemy(name="Goblin", hp=30, attack_power=5)
    combat = CombatManager(player, enemy)

    combat.fight()


if __name__ == "__main__":
    main()
