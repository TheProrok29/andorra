from django.db import models
from math import floor


class Character(models.Model):
    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'
        ordering = ('name',)

    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    _growth_points = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(null=True)
    health_points = models.IntegerField()
    strength = models.PositiveIntegerField()
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

    @property
    def growth_points(self):
        return self._growth_points

    @growth_points.setter
    def growth_points(self, value):
        self._growth_points = value
        while (self.level < 100 and self._growth_points >= self.next_level):
            self.level += 1
            self.health_points = self.level
            self.strength = floor(self.level / 3)
