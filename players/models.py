from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Player(models.Model):
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ('name',)

    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=True)
    actual_exp = models.PositiveIntegerField()
    next_level_exp = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()
    health = models.IntegerField()
    strength = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
