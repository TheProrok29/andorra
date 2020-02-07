from dataclasses import dataclass

from django.forms import model_to_dict
from django.test import TestCase
from characters.models import Character

import random

@dataclass
class FightEvent:
    attacker: str
    defender: str
    damage: int

@dataclass
class FightResults:
    winner: str


class FightTest(TestCase):

    def test_fight(self):
        hero = Character(name='jan', level=10, health_points=10, strength=3) #strength = attack
        enemy = Character(name='wilk', level=5, health_points=5, strength=1)

        for i in range(1000000):
            result = self.basic_fight(hero, enemy)
            self.assertTrue(result[-1].winner == hero.name)
            self.assertTrue(len(result) > 1)

    def basic_fight(self, hero:Character, enemy:Character):

        hero = Character(**model_to_dict(hero))
        enemy = Character(**model_to_dict(enemy))

        characters = [hero, enemy]

        attacking_character:Character = random.choice(characters)
        characters.remove(attacking_character)

        target:Character = random.choice(characters)

        fight_process = []

        while target.health_points > 0 and attacking_character.health_points > 0:
            fight_process.append(FightEvent(attacking_character,target, attacking_character.strength))
            target.health_points = target.health_points - attacking_character.strength
            fight_process.append(FightEvent(target, attacking_character, target.strength))
            attacking_character.health_points = attacking_character.health_points - target.strength

        if attacking_character.health_points > 0 :
            fight_process.append(FightResults(attacking_character.name))
        else:
            fight_process.append(FightResults(target.name))

        return fight_process







