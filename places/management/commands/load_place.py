import requests
from django.core.management.base import BaseCommand
from places.models import Image, Location
from django.core.files.base import ContentFile


def get_location_details(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    return response.json()


def get_image_bytes(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return response.content


def save_image(location, content):
    image = Image(location=location)
    image_name = "place_image_.png"
    image_file = ContentFile(content, name=image_name)
    image.image.save(image_name, image_file, save=True)


class Command(BaseCommand):
    help = "Загрузить данные о локации"

    def add_arguments(self, parser):
        parser.add_argument(
            "-u",
            "--url",
            type=str,
            help="Укажите URL с данными о локации в json-формате",
        )

    def handle(self, *args, **options):
        location_details = get_location_details(options["url"])
        location, _ = Location.objects.get_or_create(
            title=location_details["title"],
            defaults={
                "description_short": location_details["description_short"],
                "description_long": location_details["description_long"],
                "lng": location_details["coordinates"]["lng"],
                "lat": location_details["coordinates"]["lat"],
            },
        )

        for image_url in location_details["imgs"]:
            image = get_image_bytes(image_url)
            save_image(location, image)
