from dataclasses import dataclass
from math import sqrt

from django.forms import model_to_dict
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


class Fight:
    def check_if_centuria_and_go_to_fight(self, hero: Character, enemy: Character):

        hero = Character(**model_to_dict(hero))
        enemy = Character(**model_to_dict(enemy))

        if hero.level >= 100:
            result = self.advanced_fight(hero, enemy)
            return result
        else:
            return self.basic_fight(hero, enemy)

    def advanced_fight(self, hero: Character, enemy: Character):  # fight mechanics with defense and reflex

        characters = [hero, enemy]

        attacking_character: Character = random.choice(characters)
        characters.remove(attacking_character)

        target: Character = random.choice(characters)

        fight_process = []

        while target.health_points > 0 and attacking_character.health_points > 0:
            fight_process.append(FightEvent(attacking_character, target, attacking_character.strength))

            dodge = self._check_reflex(attacking_character, target)
            if not dodge:
                target.health_points -= max(attacking_character.strength - target.defense_strength, 1)

            fight_process.append(FightEvent(target, attacking_character, target.strength))

            dodge = self._check_reflex(target, attacking_character)
            if not dodge:
                attacking_character.health_points -= max(target.strength - attacking_character.defense_strength, 1)

        if attacking_character.health_points > 0:
            fight_process.append(FightResults(attacking_character.name))
        else:
            fight_process.append(FightResults(target.name))

        return fight_process

    def basic_fight(self, hero: Character, enemy: Character):

        characters = [hero, enemy]

        attacking_character: Character = random.choice(characters)
        characters.remove(attacking_character)

        target: Character = random.choice(characters)

        fight_process = []

        while target.health_points > 0 and attacking_character.health_points > 0:
            fight_process.append(FightEvent(attacking_character, target, attacking_character.strength))
            target.health_points = target.health_points - attacking_character.strength
            fight_process.append(FightEvent(target, attacking_character, target.strength))
            attacking_character.health_points = attacking_character.health_points - target.strength

        if attacking_character.health_points > 0:
            fight_process.append(FightResults(attacking_character.name))
        else:
            fight_process.append(FightResults(target.name))

        return fight_process

    def _check_reflex(self, attacking_character: Character, target: Character):

        if attacking_character.reflex < target.reflex:
            dodge_probability = 0.2 + 0.3 * sqrt(attacking_character.reflex / target.reflex)
        else:
            dodge_probability = 0.5 + 0.3 * (1 - sqrt(target.reflex / attacking_character.reflex))

        dodge = random.random() < dodge_probability

        return dodge

# this file contains basic and advanced mechanics for fitghting with one target