class Player:

    def __init__(self, name, player_class, hp=100):
        self.name = name
        self.player_class = player_class
        self.hp = hp
        self.attack_power = 10 if player_class == "Warrior" else 7
        self.defense = 5 if player_class == "Warrior" else 3

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp -= max(0, amount - self.defense)

    def attack(self):
        return self.attack_power
