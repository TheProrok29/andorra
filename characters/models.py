from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Character(models.Model):
    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'
        ordering = ('name',)

    # user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    name = models.CharField(max_length=60, unique=True)
    skill_points = models.PositiveIntegerField()                                 # now
    level = models.PositiveSmallIntegerField()                                  # now
    health_points = models.IntegerField()                                          # now
    force = models.PositiveIntegerField()                                        # now
    defense_strength = models.PositiveIntegerField(blank=True, null=True)        # future
    action_points = models.PositiveIntegerField(blank=True, null=True)         # future
    reflex = models.PositiveIntegerField(blank=True, null=True)                  # future
    dexterity = models.PositiveIntegerField(blank=True, null=True)            # future
    magic = models.PositiveIntegerField(blank=True, null=True)                   # future
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# h1 = Character(name='Prorok', skill_points=200, level=2, health_points=100, force=100)
# h1.save()

# h2 = Character(name='Prostek', skill_points=300, level=4, health_points=200, force=200, defense_strength=300, action_points=30)
# h2.save()
