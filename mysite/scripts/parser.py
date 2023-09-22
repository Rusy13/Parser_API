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
from save_file import save_to_database



sys.path.append('/home/ubunto/Desktop/SAL/mysite')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()


driver = webdriver.Chrome()

driver.get('https://opendata.mkrf.ru/opendata/7705851331-cinema')
time.sleep(7)  
page_button = driver.find_element(By.XPATH, '//div[@class="tab_button build_table"]')
page_button.click()
time.sleep(7)
page_number = 1
i = 0

while True:
    r = requests.get("https://opendata.mkrf.ru/opendata/7705851331-cinema")
    html = BS(r.content, 'html.parser')

    try:
        table = driver.find_element(By.ID, "dataset_table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')  # Используем find_elements для поиска всех td
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
                

                # print(native_name,'====',city,'====',address,'====',organization,'====',website,'====',inn,'====',latitude,'====',longitude)
                save_to_database(native_name, city, address, organization, website, inn, latitude, longitude)

                # cinema = Cinema(
                #     id=item_id,
                #     name=native_name,
                #     locale=city,
                #     website=website,
                #     email=item_email
                # )
                # cinema.save()

        next_page_button = driver.find_element(By.XPATH, '//a[@class="paginate_button next"]')
        if "disabled" in next_page_button.get_attribute("class"):
            break
        next_page_button.click()
        page_number += 1
        time.sleep(3)

    except (NoSuchElementException, StaleElementReferenceException):
        break

driver.quit()

print(i,'===== iiiiiiiiiiiiiiiiiiiiiii')