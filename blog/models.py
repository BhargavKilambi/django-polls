from django.db import models

# Create your models here.
class Contestant(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    picurl = models.CharField(max_length=500)
    votes = models.IntegerField()
    desp = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Vote(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
