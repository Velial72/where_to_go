from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='название', unique=True)
    short_description = models.TextField(verbose_name='короткое описание', blank=True)
    long_description = HTMLField(verbose_name='описание', blank=True)
    lng = models.FloatField(verbose_name='долгота')
    lat = models.FloatField(verbose_name='широта')

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self) -> str:
        return self.title
  

class Image(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='место', related_name='images')
    image = models.ImageField(verbose_name='картинка', upload_to='')
    position = models.IntegerField(verbose_name='позиция', db_index=True, default=0)

    class Meta:
        ordering = ['position']
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'
        unique_together = ('image', 'title')
