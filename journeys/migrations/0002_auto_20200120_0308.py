# Generated by Django 3.0.1 on 2020-01-20 02:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

from characters.models import Character


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200111_1550'),
        ('journeys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activejourney',
            name='character',
            field=models.ForeignKey(
                default=lambda: Character.objects.filter().first(),
                on_delete=django.db.models.deletion.CASCADE,
                to='characters.Character'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activejourney',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
