from django.db import models
from django.db.models.deletion import CASCADE
from picklefield.fields import PickledObjectField
from django.utils import timezone
from datetime import timedelta
from characters.models import Character


class ActiveJourney(models.Model):
    character = models.OneToOneField(Character, CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField()
    log = PickledObjectField()
    active = models.BooleanField(default=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.end_date


def toggle_journey_log_visibility(journey: ActiveJourney):
    journey.is_visible = not journey.is_visible
    journey.save()


def show_finished_journey_event_step(journey: ActiveJourney, now_date: timezone) -> ActiveJourney.log:
    log_part = []
    total = 0
    if now_date > journey.end_date:
        return journey.log
    for i, _ in enumerate(journey.log):
        total += journey.log[i].duration
        if now_date > journey.start_date + timedelta(seconds=total):
            log_part.append(journey.log[i])
    return log_part
