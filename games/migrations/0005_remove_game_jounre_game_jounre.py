# Generated by Django 5.0.1 on 2024-02-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_game_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='jounre',
        ),
        migrations.AddField(
            model_name='game',
            name='jounre',
            field=models.ManyToManyField(to='games.jounre'),
        ),
    ]