import requests
from bs4 import BeautifulSoup as BS
import sys
import os
import django
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
from selenium.webdriver.support.ui import Select


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# sys.path.append('../')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.mysite.settings')

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

driver = webdriver.Chrome()

driver.get('https://opendata.mkrf.ru/opendata/7705851331-cinema')
time.sleep(7)

page_button = driver.find_element(By.XPATH, '//div[@class="tab_button build_table"]')
page_button.click()
time.sleep(7)

select_element = driver.find_element(By.ID, 'table_length')
select = Select(select_element)
select.select_by_visible_text('100')
time.sleep(5)


page_number = 1
i = 0


while True:
    r = requests.get("https://opendata.mkrf.ru/opendata/7705851331-cinema")
    html = BS(r.content, 'html.parser')

    try:
        table = driver.find_element(By.ID, "dataset_table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if cells:
                native_name = cells[0].find_element(By.TAG_NAME, 'span').text
                city = cells[1].find_element(By.TAG_NAME, 'span').text
                address = cells[2].find_element(By.TAG_NAME, 'span').text
                organization = cells[3].find_element(By.TAG_NAME, 'span').text
                website = cells[4].find_element(By.TAG_NAME, 'span').text
                inn = cells[5].find_element(By.TAG_NAME, 'span').text
                latitude = cells[6].find_element(By.TAG_NAME, 'div').get_attribute('data-lat')
                longitude = cells[6].find_element(By.TAG_NAME, 'div').get_attribute('data-lng')
                i += 1
                print(native_name, city, address, organization, website, inn, latitude, longitude)
                save_to_database(native_name, city, address, organization, website, inn, latitude, longitude)

        next_page_button = driver.find_element(By.XPATH, '//a[@class="paginate_button next"]')
        if "disabled" in next_page_button.get_attribute("class"):
            break
        next_page_button.click()
        page_number += 1
        time.sleep(3)

    except (NoSuchElementException, StaleElementReferenceException):
        break

driver.quit()