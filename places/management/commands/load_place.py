import json
import logging
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandParser

from places.models import Image, Place


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


class Command(BaseCommand):
    help = 'Загрузка локаций из json-файлов'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('json_urls', nargs='+', help='URLs to the JSON files')

    def handle(self, *args, **options):
        json_urls = options['json_urls']
        for json_url in json_urls:
            try:
                place_response = requests.get(json_url, timeout=60)
                place_response.raise_for_status()
                place = place_response.json()

                defaults = dict(
                    title=place['title'],
                    description_short=place['description_short'],
                    description_long=place['description_long'],
                    lng=place['coordinates']['lng'],
                    lat=place['coordinates']['lat']
                )
                added_place, place_created = Place.objects.update_or_create(
                    title=place['title'],
                    defaults=defaults
                )

                images = place.get('imgs', [])
                for image_url in images:
                    try:
                        image_response = requests.get(image_url, timeout=120)
                        image_response.raise_for_status()
                        image_name = urlparse(image_url).path.split('/')[-1]
                        Image.objects.create(
                            title=added_place,
                            image = ContentFile(image_response.content, name=image_name)
                        )
                    except requests.RequestException as e:
                        logging.error(f"Error fetching image {image_url}: {e}")

                if not place_created:
                    logging.info(f'Place "{added_place}" was already added earlier')
                    continue
                logging.info(f'New place "{added_place}" added')

            except requests.RequestException as e:
                logging.error(f"Error fetching JSON from {json_url}: {e}")
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON from {json_url}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error: {e}")