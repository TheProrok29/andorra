# Generated by Django 3.0.1 on 2020-01-22 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_character_busy'),
        ('journeys', '0005_auto_20200121_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activejourney',
            name='character',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='characters.Character'),
        ),
    ]
