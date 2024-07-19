'''
This file contains the BattleUnit class which represents a warrior unit in the game.
'''
class BattleUnit:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    def take_damage(self, damage):
        # Reduce unit's health by the given damage
        self.health -= damage
    def attack_unit(self, target):
        # Attack another unit
        target.take_damage(self.attack)
    # Other unit-related methods and properties