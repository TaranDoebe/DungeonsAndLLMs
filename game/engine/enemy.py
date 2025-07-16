class Enemy:
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp -= amount

    def attack(self):
        return self.attack_power
