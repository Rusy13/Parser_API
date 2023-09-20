import requests
from save_file import save_to_database

# Замените 'YOUR_API_KEY_HERE' на ваш реальный API ключ
api_key = '9311adde05f18107c8ddaf5f88f72024c1c50a6cd2497dcd4823200c00e5f5e4'

# URL API
url = 'https://opendata.mkrf.ru/v2/cinema/75?l=1000'

# Заголовки запроса с API ключом и указанием формата JSON
headers = {
    'Accept': 'application/json',
    'X-API-KEY': api_key,
}

# Выполнение GET-запроса к API
try:
    response = requests.get(url, headers=headers)

    # Проверка на успешный статус ответа (200 OK)
    if response.status_code == 200:
        # Получение данных в формате JSON
        data = response.json()
        i = 0

        # Дальнейшая обработка данных
        for item in data.get('data', []):
            item_id = item.get('data', {}).get('general', {}).get('id')
            item_name = item.get('data', {}).get('general', {}).get('name')
            item_locale = item.get('data', {}).get('general', {}).get('locale', {}).get('name')
            item_website = item.get('data', {}).get('general', {}).get('contacts', {}).get('website')
            item_email = item.get('data', {}).get('general', {}).get('contacts', {}).get('email')
            
            save_to_database(item_id, item_name, item_locale, item_website, item_email)
            print(f'ID: {item_id}, Name: {item_name}, Locale: {item_locale}, Website: {item_website}, Email: {item_email},')
            i+=1
        print('qewrqwer =', i)
    else:
        print(f'Ошибка при выполнении запроса: {response.status_code}')
except Exception as e:
    print(f'Произошла ошибка: {str(e)}')