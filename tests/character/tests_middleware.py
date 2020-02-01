from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from characters.models import Character
from characters.middleware import InceptionMiddleware


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
        character.growth_points = 704
        character.save()

        self.client.get('/statistics/')

        character.refresh_from_db()
        self.assertEqual(character.level, 50)
        self.assertEqual(character.health_points, 50)
        self.assertEqual(character.strength, 16)
