from mysite.cinema.models import Cinema

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
