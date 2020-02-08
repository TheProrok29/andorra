from django.test import TestCase

from characters.models import Character


class LevelingTest(TestCase):

    def test_level_up(self):
        self.client.get('/statistics/')
        character = Character.objects.get(id=1)
        character.growth_points = 704
        character.save()

        self.client.get('/statistics/')

        character.refresh_from_db()
        self.assertEqual(character.level, 51)
        self.assertEqual(character.health_points, 51)
        self.assertEqual(character.strength, 17)
