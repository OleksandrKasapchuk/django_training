# Generated by Django 5.0.1 on 2024-02-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_game_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
