from django.db import models


class Ant(models.Model):
    name = models.CharField(default='', blank=True)
    description = models.TextField()


class Beetle(models.Model):
    name = models.CharField(default='', blank=True)
    description = models.TextField()
