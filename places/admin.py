from django.contrib import admin
from .models import Image, Location
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    fields = ("image", "image_preview", "order")
    readonly_fields = ["image_preview"]
    ordering = ["order"]


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ("id", "title", "short_description", "lng", "lat")
    search_fields = ("title",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    list_filter = ("location",)
    ordering = ("location", "order")
