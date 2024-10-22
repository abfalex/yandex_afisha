import sys
import requests
from django.core.management.base import BaseCommand
from places.models import Image, Location
from django.core.files.base import ContentFile
from django.core.exceptions import MultipleObjectsReturned
from requests.exceptions import HTTPError, ConnectionError
import time

def get_location_details(json_url):
    response = requests.get(json_url)
    response.raise_for_status()
    return response.json()


def get_image_bytes(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return response.content


def save_image(location, content):
    image = ContentFile(content, name="place_image_.png")
    Image.objects.create(location=location, image=image)


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

        try:
            location, _ = Location.objects.get_or_create(
                title=location_details["title"],
                defaults={
                    "short_description": location_details["description_short"],
                    "long_description": location_details["description_long"],
                    "lng": location_details["coordinates"]["lng"],
                    "lat": location_details["coordinates"]["lat"],
                },
            )
        except MultipleObjectsReturned:
            sys.stderr.write(f"Найдено несколько записей для локации с названием {location_details['title']}.")
            return

        for image_url in location_details["imgs"]:
            retry_count = 0
            max_retries = 3
            while retry_count < max_retries:
                try:
                    image = get_image_bytes(image_url)
                    save_image(location, image)
                except HTTPError as e:
                    sys.stderr.write(f"HTTP ошибка при загрузке изображения {image_url}: {e}\n")
                    break
                except ConnectionError as e:
                    sys.stderr.write(f"Ошибка соединения при загрузке изображения {image_url}: {e}\n")
                    retry_count += 1
                    if retry_count < max_retries:
                        time.sleep(5)
                    else:
                        sys.stderr.write(f"Изображение {image_url} не удалось загрузить после {max_retries} попыток.\n")
                        break