import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django.settings")
django.setup()

from games.models import Game, Jounre

jounre1 = Jounre(name="shooter")
jounre1.save()
jounre2 = Jounre(name="horror")
jounre2.save()
game = Game.objects.get(id=6)
game.jounre.add(jounre1)
game.jounre.add(jounre2)
