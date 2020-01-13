from django.db import models
from datetime import datetime
from datetime import timedelta


class ActiveJourney(models.Model):
    journey_end = models.DateTimeField()
    end_date = datetime.now() + timedelta(seconds=20)

    def __str__(self):
        return self.journey_end
