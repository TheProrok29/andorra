from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory

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
