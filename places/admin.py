from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from .models import Place, Image


class AdminImageInline(SortableStackedInline):
    model = Image
    extra = 1
    readonly_fields = ['preview_image']


    def preview_image(self, obj):
        if obj:
            return format_html('<img src="{}" style="max-height: 200px; max-width: 100%;" />', obj.image.url)
        else:
            return 'картинки нет'
        


@admin.register(Place)
class AdminPlace(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title']

    inlines = [
        AdminImageInline
    ]


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    '''Admin panel for Image model'''
    list_display = ['title',]