import sys
import os
import django

sys.path.append('/home/ubunto/Desktop/SAL/mysite')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django.setup()

from cinema.models import Cinema


def save_to_database(item_name, item_locale, item_street, item_legal_entity, item_website, item_inn, item_latitude, item_longitude):
    cinema = Cinema(
        name=item_name,
        locale=item_locale,
        street=item_street,
        legal_entity=item_legal_entity,
        website=item_website,
        inn=item_inn,
        latitude=item_latitude,
        longitude=item_longitude
    )
    cinema.save()