from django.test import TestCase, override_settings


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/statistics/')
        self.assertTemplateUsed(response, 'statistics.html')