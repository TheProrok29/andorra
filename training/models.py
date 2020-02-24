from django.db import models
from django.db.models.deletion import CASCADE
from characters.models import Character
from datetime import datetime, timezone, timedelta


class Training(models.Model):
    character = models.OneToOneField(Character, CASCADE, blank=True, null=True)
    start_training_date = models.DateTimeField(auto_now_add=True)
    end_training_date = models.DateTimeField(blank=True, null=True)
    number_completed_training = models.PositiveIntegerField(default=0)
    is_ending = models.BooleanField(default=False)

    def __str__(self):
        return self.character.name


def create_trainning(character: Character):
    toogle_character_busy(character)
    new_training = Training()
    new_training.character = character
    new_training.is_ending = False
    new_training.save()
    return new_training


def delete_training(character: Character):
    toogle_character_busy(character)
    training = Training.objects.filter(character=character).first()
    return training.delete()


def set_is_ending_training(training: Training):
    training_done_counter, actual_training_rest = count_number_of_trainings(training)
    training.end_training_date = datetime.now(timezone.utc) + timedelta(seconds=20)
    training.is_ending = True
    training.number_completed_training = training_done_counter
    training.save()


def toogle_character_busy(character: Character):
    character.busy = not character.busy
    character.save()


def count_number_of_trainings(training: Training):
    time_now = datetime.now(timezone.utc)
    diff = time_now - training.start_training_date
    return diff.seconds // 20, diff.seconds % 20


def add_training_points_to_character(character: Character):
    if(character.busy):
        training = Training.objects.filter(character=character).first()
        character.growth_points += training.number_completed_training + 1
        character.save()
        return True
