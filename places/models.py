from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField("Название", max_length=255)
    short_description = models.TextField("Короткое описание", blank=True, null=True)
    long_description = HTMLField("Подробное описание", blank=True, null=True)
    lng = models.DecimalField(
        "Долгота", max_digits=20, decimal_places=14, blank=True, null=True
    )
    lat = models.DecimalField(
        "Широта", max_digits=20, decimal_places=14, blank=True, null=True
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(
        Location, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField("Изображение", upload_to="images/")
    order = models.PositiveIntegerField("Порядок", default=0)

    def image_preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-height: 200px;"/>', self.image.url
            )
        return ""

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order} {self.location.title}"
