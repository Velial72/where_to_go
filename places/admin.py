from django.contrib import admin
from .models import Place, Image


class AdminImageInline(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Place)
class AdminPlace(admin.ModelAdmin):
    list_display = ['title']
    inlines = [
        AdminImageInline
    ]
