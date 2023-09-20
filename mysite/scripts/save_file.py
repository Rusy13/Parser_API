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


sys.path.append('/home/ubunto/Desktop/SAL/mysite')
from cinema.models import Cinema
# from mysite.cinema.models import Cinema


def save_to_database(item_id, item_name, item_locale, item_website, item_email):
    # Создание объекта Cinema и сохранение в базу данных
    cinema = Cinema(
        id=item_id,
        name=item_name,
        locale=item_locale,
        website=item_website,
        email=item_email
    )
    cinema.save()
