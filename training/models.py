from django.db import models


class Training(models.Model):
    start_training_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.start_training_date
