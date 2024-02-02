from django.db import models

# Create your models here.
class Jounre(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=50)
    jounre = models.ManyToManyField(Jounre)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
