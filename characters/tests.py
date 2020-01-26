from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory

from .models import Character
from .middleware import InceptionMiddleware


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/statistics/')
        self.assertTemplateUsed(response, 'statistics.html')


class MiddlewareTest(TestCase):

    def test_character_creation(self):
        sut = InceptionMiddleware(lambda r: None)
        request_factory = RequestFactory()
        session_middleware = SessionMiddleware()
        request = request_factory.get('/')
        session_middleware.process_request(request)
        sut(request)
        self.assertIsNotNone(request.session['character_id'])


class LevelingTest(TestCase):

    def test_level_up(self):
        self.client.get('/statistics/')
        character = Character.objects.get(id=1)
        character.skill_points = 704
        character.save()

        self.client.get('/statistics/')

        character.refresh_from_db()
        self.assertEqual(character.level, 50)
        self.assertEqual(character.health_points, 50)
        self.assertEqual(character.force, 16)
