from django.test import TestCase
from training.models import Training
from characters.models import Character


class TrainingCreateTest(TestCase):

    def test_training_creation(self):
        hero = Character.objects.create(name='jan', level=10, health_points=10, strength=3)
        training = Training()
        training.character = hero
        training.save()
        self.assertTrue(isinstance(training, Training))
        self.assertEqual(training.__str__(), hero.name)
        self.assertIsNotNone(training.start_training_date)
        self.assertEqual(training.end_training_date, None)
        self.assertEqual(training.number_completed_training, 0)
        self.assertEqual(training.is_ending, False)
