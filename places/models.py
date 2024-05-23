from django.db import models

class Place(models.Model):
  title = models.CharField(max_length=200)
  place_id = models.CharField(max_length=200, unique=True)
  description_short = models.TextField()
  description_long = models.TextField()
  lng = models.FloatField(max_length=200)
  lat = models.FloatField(max_length=200)

  def __str__(self) -> str:
    return self.title

class Image(models.Model):
  title = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='фотографии', related_name='images')
  image = models.ImageField()