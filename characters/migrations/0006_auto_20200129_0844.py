# Generated by Django 3.0.1 on 2020-01-29 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_merge_20200126_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='skill_points',
            new_name='growth_points',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='force',
            new_name='strength',
        ),
    ]
