from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, override_settings, RequestFactory

from .middleware import InceptionMiddleware


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
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
        self.assertIsNotNone(request.character)
        self.assertIsNot(request.character.name, '')
