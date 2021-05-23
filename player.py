from enemy import Enemy
from entity import Entity
from enemy import Enemy
import typing
import random

class Player(Entity):
    def __init__(self, id, display_name, health, damage, crit_chance=40):
        super().__init__(id, display_name, immune=False)
        self.health = health
        self.damage = damage
        self.crit_chance = crit_chance

    def die(self, killer: Enemy) -> None:
        print(f"{self.display_name} has been killed by {killer.display_name}")
        self.destroy()

    def attack(self, target: Entity) -> None:
        if random.randint(0, 100) > self.crit_chance:
            damage = self.damage * 2
        print(f"{self.display_name} has attacked {target.display_name}. The attack dealt {damage} damage.")
        target.health -= damage
        if target.health <= 0:
            target.die(self)