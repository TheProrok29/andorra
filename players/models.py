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


# p1 = Player(name='Prorok', actual_exp=200, next_level_exp=400, level=2, health=100, strength=100)
# p1.save()
# p2 = Player(name='BigBoss', actual_exp=300, next_level_exp=400, level=3, health=105, strength=110)
# p2.save()
