from django.db import models


class Location(models.Model):
    title = models.CharField("Название", max_length=255)
    description_short = models.TextField("Короткое описание", blank=True, null=True)
    description_long = models.TextField("Подробное описание", blank=True, null=True)
    longitude = models.DecimalField("Долгота", max_digits=20, decimal_places=14)
    latitude = models.DecimalField("Широта", max_digits=20, decimal_places=14)

    def __str__(self):
        return self.title
