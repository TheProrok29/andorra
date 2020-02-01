from django.db import models
from math import floor
# from django.contrib.auth.models import User


class Character(models.Model):
    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'
        ordering = ('name',)

    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    growth_points = models.PositiveIntegerField(default=0)                        # now
    level = models.PositiveSmallIntegerField()                                  # now
    health_points = models.IntegerField()                                          # now
    strength = models.PositiveIntegerField()                                        # now
    defense_strength = models.PositiveIntegerField(blank=True, null=True)        # future
    action_points = models.PositiveIntegerField(blank=True, null=True)         # future
    reflex = models.PositiveIntegerField(blank=True, null=True)                  # future
    dexterity = models.PositiveIntegerField(blank=True, null=True)            # future
    magic = models.PositiveIntegerField(blank=True, null=True)                   # future
    created = models.DateTimeField(auto_now_add=True)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def next_level(self):
        next_level_points = floor(6 * (1.1 ** self.level))
        return next_level_points
