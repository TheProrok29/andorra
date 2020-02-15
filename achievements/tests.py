from django.test import TestCase
from bs4 import BeautifulSoup

from characters.models import Character


class Achievements(TestCase):

    def test_view_achievements(self):
        response = self.client.get('/achievements/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'achievements.html')

    def test_achievements(self):
        hero = Character.objects.create(name='jan', health_points=10, strength=5)

        response = self.client.get('/achievements/')
        soup = BeautifulSoup(response.content, features='html.parser')
        self.assertIsNone(soup.select_one('.achievement'))

        hero = Character.objects.get(id=self.client.session['character_id'])
        hero.growth_points = 1
        hero.save()
        response = self.client.get('/achievements/')
        soup = BeautifulSoup(response.content, features='html.parser')
        self.assertIsNotNone(soup.select_one('.achievement'))
