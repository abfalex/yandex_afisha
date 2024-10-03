from tabnanny import verbose
from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField("Название", max_length=255)
    short_description = models.TextField("Короткое описание", blank=True)
    long_description = HTMLField("Подробное описание", blank=True)
    lng = models.DecimalField("Долгота", max_digits=20, decimal_places=14)
    lat = models.DecimalField("Широта", max_digits=20, decimal_places=14)

    class Meta:
        unique_together = ["title"]

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(
        Location,
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Локация",
    )
    image = models.ImageField("Изображение", upload_to="images/")
    order = models.PositiveIntegerField("Порядок", default=0, db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order} {self.location.title}"

    def image_preview(self):
        if self.image:
            return format_html(
                '<img src="{}" style="max-width: 200px;"/>', self.image.url
            )
        return ""
