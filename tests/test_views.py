from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class JourneysPageTest(TestCase):

    def test_uses_journeys_template(self):
        response = self.client.get('/journeys/')
        self.assertTemplateUsed(response, 'journeys.html')
