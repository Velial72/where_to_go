from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']