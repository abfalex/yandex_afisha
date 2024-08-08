from django.contrib import admin
from .models import Image, Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("title", "description_short", "longitude", "latitude")


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ("image", "order")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("location", "image", "order")
    list_filter = ("location",)
    ordering = ("location", "order")
