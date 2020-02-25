from characters.models import Character
from training.models import Training
from training.models import create_trainning, delete_training, set_is_ending_training, toogle_character_busy
from training.models import count_number_of_trainings, add_training_points_to_character
from django.test import TestCase
from datetime import datetime, timezone, timedelta


class TrainingFunctionsTest(TestCase):
    def setUp(self):
        self.hero = Character.objects.create(name='jan', level=1, health_points=10, strength=3)

    def test_create_training(self):
        training = create_trainning(self.hero)

        self.assertTrue(isinstance(training, Training))
        self.assertEqual(training.__str__(), self.hero.name)
        self.assertIsNotNone(training.start_training_date)
        self.assertEqual(training.end_training_date, None)
        self.assertEqual(training.number_completed_training, 0)
        self.assertEqual(training.is_ending, False)

    def test_delete_training(self):
        training = Training()
        training.character = self.hero
        training.save()
        self.assertEqual(Training.objects.filter(character=self.hero).count(), 1)
        self.assertTrue(delete_training(self.hero))
        self.assertEqual(Training.objects.filter(character=self.hero).count(), 0)

    def test_toogle_character_busy(self):
        self.assertEqual(self.hero.busy, False)
        toogle_character_busy(self.hero)
        self.assertEqual(self.hero.busy, True)
        toogle_character_busy(self.hero)
        self.assertEqual(self.hero.busy, False)

    def test_set_is_ending_training(self):
        training = create_trainning(self.hero)
        self.assertIsNone(training.end_training_date)
        self.assertEqual(training.is_ending, False)
        set_is_ending_training(training)
        self.assertIsNotNone(training.end_training_date)
        self.assertEqual(training.is_ending, True)

    def test_count_number_of_trainings(self):
        training = Training()
        start = datetime.now(timezone.utc) - timedelta(seconds=405)
        training.save()
        training.start_training_date = start
        training.save()
        number, rest = count_number_of_trainings(training)
        self.assertEqual(number, 20)
        self.assertEqual(rest, 5)

    def test_add_training_points_to_character(self):
        training = Training()
        training.character = self.hero
        training.save()
        training.start_training_date = datetime.now(timezone.utc) - timedelta(seconds=885)
        training.save()
        self.hero.busy = True
        set_is_ending_training(training)
        add_training_points_to_character(self.hero)
        self.assertEqual(self.hero.growth_points, 45)
