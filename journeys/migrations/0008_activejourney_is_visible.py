# Generated by Django 3.0.1 on 2020-02-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0007_activejourney_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='activejourney',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]