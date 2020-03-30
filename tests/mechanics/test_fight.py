import random

from django.test import TestCase
from characters.models import Character
from mechanics.fight import Fight


class FightTest(TestCase):
    def test_fight(self):
        random.seed(2137)
        hero = Character(
            name='jan', level=100, health_points=10, strength=5, defense_strength=3, reflex=3
        )  # strength = attack
        enemy = Character(name='wilk', level=5, health_points=5, strength=1, defense_strength=2, reflex=2)

        for _ in range(100):
            result = Fight().check_if_centuria_and_go_to_fight(hero, enemy)
            self.assertTrue(result[-1].winner == hero.name)
            self.assertTrue(len(result) > 1)
