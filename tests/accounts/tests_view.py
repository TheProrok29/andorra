from django.test import TestCase, override_settings, Client
from django.contrib.auth.models import User


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TemplateTestBeforeLogin(TestCase):

    def test_view_uses_signup_template(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_view_uses_login_template(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TemplateTestAfterLogin(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.c = Client()

    def test_view_journeys_template_after_login(self):
        response = self.c.post('/accounts/login/', self.credentials, follow=True)
        response = self.c.get('/journeys/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journeys.html')

    def test_view_training_template_after_login(self):
        response = self.c.post('/accounts/login/', self.credentials, follow=True)
        response = self.c.get('/training/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training.html')

    def test_view_statistics_template_after_login(self):
        response = self.c.post('/accounts/login/', self.credentials, follow=True)
        response = self.c.get('/statistics/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statistics.html')
