import sys
import os
import django

# Добавьте путь к вашему Django проекту в список путей Python
sys.path.append('/home/ubunto/Desktop/SAL/mysite')

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE на ваш файл settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Загружаем настройки Django
django.setup()

# Дальше ваш код
from cinema.models import Cinema


def save_to_database(item_name, item_locale, item_street, item_legal_entity, item_website, item_inn, item_latitude, item_longitude):
    # Создание объекта Cinema и сохранение в базу данных
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