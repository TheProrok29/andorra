from django.db import models
from django.db.models.deletion import CASCADE
from picklefield.fields import PickledObjectField

from characters.models import Character


class ActiveJourney(models.Model):
    character = models.OneToOneField(Character, CASCADE)
    end_date = models.DateTimeField()
    log = PickledObjectField()
    active = models.BooleanField(default=True)
    slug = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.end_date
