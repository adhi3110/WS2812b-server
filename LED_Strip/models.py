from django.db import models

# Create your models here


class Colour(models.Model):
    name = models.CharField(max_length=200)
    red = models.IntegerField()
    blue = models.IntegerField()
    green = models.IntegerField()
    power = models.BooleanField()

    def __str__(self):
        return self.name
