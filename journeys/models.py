from django.db import models
from datetime import datetime
from datetime import timedelta


class ActiveJourney(models.Model):
    end_date = datetime.now() + timedelta(seconds=20)
