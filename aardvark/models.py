from django.db import models


class Ant(models.Model):
    name = models.CharField(null=True, blank=False)
    description = models.CharField(max_length=5000)


class Beetle(models.Model):
    name = models.CharField(null=True, blank=False)
    description = models.CharField(max_length=5000)
