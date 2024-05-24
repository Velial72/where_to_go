from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
  title = models.CharField(max_length=200, verbose_name='название', unique=True)
  # place_id = models.CharField(max_length=200, unique=True)
  description_short = models.TextField(verbose_name='короткое описание')
  description_long = HTMLField(verbose_name='описание')
  lng = models.FloatField(max_length=200, verbose_name='долгота')
  lat = models.FloatField(max_length=200, verbose_name='широта')

  class Meta:
    verbose_name = 'место'
    verbose_name_plural = 'места'

  def __str__(self) -> str:
    return self.title
  

class Image(models.Model):
  title = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='место', related_name='images')
  image = models.ImageField(verbose_name='картинка', upload_to='')
  position = models.IntegerField(verbose_name='позиция', db_index=True, default=0)

  def save(self, *args, **kwargs):
    if not self.position:
        last_position = Image.objects.filter(title=self.title).aggregate(models.Max('position'))['position__max']
        self.position = (last_position or 0) + 1
    super().save(*args, **kwargs)
    
  class Meta:
      ordering = ['position']
      verbose_name = 'картинка'
      verbose_name_plural = 'картинки'
      unique_together = ('image', 'title')
