from django.db import models
from django.db.models.deletion import CASCADE
from characters.models import Character


class Training(models.Model):
    character = models.OneToOneField(Character, CASCADE, blank=True, null=True)
    start_training_date = models.DateTimeField(auto_now_add=True)
    end_training_date = models.DateTimeField(blank=True, null=True)
    number_completed_training = models.PositiveIntegerField(default=0)
    is_ending = models.BooleanField(default=False)

    def __str__(self):
        return self.character.name


def start_trainning(character: Character):
    character.busy = True
    character.save()
    new_training = Training()
    new_training.character = character
    new_training.is_ending = False
    new_training.save()
    return new_training


def stop_training(character: Character):
    character.busy = False
    character.save()
    training = Training.objects.filter(character=character).first()
    return training.delete()
