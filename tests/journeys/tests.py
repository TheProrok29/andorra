from datetime import timedelta
from unittest.mock import patch

from django.test import TestCase, override_settings
from bs4 import BeautifulSoup
from django.utils import timezone


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class JourneysTest(TestCase):

    def test_first_journey(self):
        response = self.client.post('/journeys/', {'journey_id': 'first_journey'}, follow=True)
        soup = BeautifulSoup(response.content, features='html.parser')
        self.assertIsNotNone(soup.select_one('.countdown'))

    def test_starting_multiple_journeys(self):
        self.client.post('/journeys/', {'journey_id': 'first_journey'}, follow=True)
        response = self.client.post('/journeys/', {'journey_id': 'first_journey'}, follow=True)
        self.assertEqual(response.status_code, 500)

    def test_journey_finish(self):
        self.client.post('/journeys/', {'journey_id': 'first_journey'})

        fake_now = timezone.now() + timedelta(seconds=30)
        with patch('django.utils.timezone.now') as mock:
            mock.return_value = fake_now
            response = self.client.get('/journeys/')
            soup = BeautifulSoup(response.content, features='html.parser')
            self.assertIsNone(soup.select_one('.countdown'))
