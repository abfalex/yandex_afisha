from django.contrib import admin
from .models import Image, Location


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ("image", "image_preview", "order")
    readonly_fields = ["image_preview"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ("title", "description_short", "lng", "lat")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    list_filter = ("location",)
    ordering = ("location", "order")
