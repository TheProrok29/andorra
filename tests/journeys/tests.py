from datetime import timedelta
from unittest.mock import patch, Mock
import datetime
from django.test import TestCase, override_settings
from bs4 import BeautifulSoup
from django.utils import timezone
from journeys.models import ActiveJourney, show_finished_journey_event_step
from journeys.definitions import JourneyEvent


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

    def test_show_finished_journey_event_step_if_two_event_finished(self):
        log = [JourneyEvent(duration=5, description='first'), JourneyEvent(
            duration=10, description='fight'), JourneyEvent(duration=5, description='second')]
        start_date = datetime.datetime(2015, 6, 15, 14, 45, 9, 182703)
        now_date = datetime.datetime(2015, 6, 15, 14, 45, 26, 182703)
        end_date = datetime.datetime(2015, 6, 15, 14, 45, 29, 182703)
        journey = Mock(spec=ActiveJourney.objects)
        journey.start_date = start_date
        journey.end_date = end_date
        journey.log = log
        self.assertEqual([JourneyEvent(duration=5, description='first'), JourneyEvent(
            duration=10, description='fight')], show_finished_journey_event_step(journey, now_date))

    def test_show_finished_journey_event_step_if_no_event_finished(self):
        log = [JourneyEvent(duration=5, description='first'), JourneyEvent(
            duration=10, description='fight'), JourneyEvent(duration=5, description='second')]
        start_date = datetime.datetime(2015, 6, 15, 14, 45, 9, 182703)
        now_date = datetime.datetime(2015, 6, 15, 14, 45, 11, 182703)
        end_date = datetime.datetime(2015, 6, 15, 14, 45, 29, 182703)
        journey = Mock(spec=ActiveJourney.objects)
        journey.start_date = start_date
        journey.end_date = end_date
        journey.log = log
        self.assertEqual([], show_finished_journey_event_step(journey, now_date))
