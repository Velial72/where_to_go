from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from places.models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html('<img src="{}" width="200" height="200" />',
                           obj.file.url
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ["title", "lng", "lat"]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'file_position']
