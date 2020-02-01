from django.test import TestCase
from characters.models import Character


class CharacterCreateTest(TestCase):

    def test_character_creation(self):
        hero = Character.objects.create(name='jan', level=10, health_points=10, strength=3)
        self.assertTrue(isinstance(hero, Character))
        self.assertEqual(hero.__str__(), hero.name)
