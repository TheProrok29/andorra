from django.test import TestCase, override_settings
from django.contrib.auth.models import User


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_user_loggin_success(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_user_loggin_false(self):
        response = self.client.post('/accounts/login/', {
            'username': 'testuser',
            'pasdsword': 'secret2'}, follow=True)
        self.assertFalse(response.context['user'].is_active)
