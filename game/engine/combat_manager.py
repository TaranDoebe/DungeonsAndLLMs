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
                self.enemy.take_damage(damage)
                print(f"You hit {self.enemy.name} for {damage} damage!")
                if not self.enemy.is_alive():
                    print(f"{self.enemy.name} has been defeated!")
                    break

                retaliation = self.enemy.attack()
                self.player.take_damage(retaliation)
                print(f"{self.enemy.name} hits you for {retaliation} damage!")

                print(f"Your HP: {self.player.hp}, Enemy HP: {self.enemy.hp}")
            elif action == 'r':
                print("You ran away!")
                break
            else:
                print("Invalid input.")

        if not self.player.is_alive():
            print("You have fallen in battle...")
