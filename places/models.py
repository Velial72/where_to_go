from django.db import models

class Place(models.Model):
  title = models.CharField(max_length=200)
  description_short = models.TextField()
  description_long = models.TextField()
  lng = models.FloatField(max_length=200)
  lat = models.FloatField(max_length=200)
