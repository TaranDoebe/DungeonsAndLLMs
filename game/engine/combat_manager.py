class CombatManager:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fight(self):
        print(f"A wild {self.enemy.name} appears!")
        while self.player.is_alive() and self.enemy.is_alive():
            action = input("Do you want to (a)ttack or (r)un? ").lower()
            if action == 'a':
                damage = self.player.attack()
                enemy_starting_hp = self.enemy.hp
                self.enemy.take_damage(damage)
                actual_enemy_damage = enemy_starting_hp - self.enemy.hp
                print(f"You hit {self.enemy.name} for {actual_enemy_damage} damage!")
                if not self.enemy.is_alive():
                    print(f"{self.enemy.name} has been defeated!")
                    break

                retaliation = self.enemy.attack()
                player_starting_hp = self.player.hp
                self.player.take_damage(retaliation)
                actual_player_damage = player_starting_hp - self.player.hp
                print(f"{self.enemy.name} hits you for {actual_player_damage} damage!")

                print(f"Your HP: {self.player.hp}, Enemy HP: {self.enemy.hp}")
            elif action == 'r':
                print("You ran away!")
                break
            else:
                print("Invalid input.")

        if not self.player.is_alive():
            print("You have fallen in battle...")
