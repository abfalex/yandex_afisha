from django.db import models


class Location(models.Model):
    title = models.CharField("Название", max_length=255)
    description_short = models.TextField("Короткое описание", blank=True, null=True)
    description_long = models.TextField("Подробное описание", blank=True, null=True)
    longitude = models.DecimalField("Долгота", max_digits=20, decimal_places=14)
    latitude = models.DecimalField("Широта", max_digits=20, decimal_places=14)

    def __str__(self):
        return self.title


class Image(models.Model):
    location = models.ForeignKey(
        Location, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField("Изображение", upload_to="images/")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.location.title} - {self.id}"
