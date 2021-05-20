import requests
from bs4 import BeautifulSoup
import csv
import os
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko', 'accept': '*/*'}
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all('div', class_='e15hqrm30')
    if pages:
        print(int(pages[-1].get_text()))
        return int(pages[-1].get_text())
    else:
        return 1

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a')

    cars = []

    for item in items:
        attr = item.get('data-ftid')
        if attr == "bulls-list_bull":
            cars.append(
                {'title': item.find('span').get_text(strip=True),
                 'link': item.get('href'),
                 'price': item.find('span', class_='css-jnatj e162wx9x0').get_text(strip=True).replace('q', ''),
                 'city': item.find('span', class_='css-17qid0e e162wx9x0').get_text(strip=True),
                 'info': item.find('div', class_='css-1duptnh e162wx9x0').get_text(strip=True),
           })
    return cars

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter= ';')
        writer.writerow(['Марка', 'ссылка', 'Цена', 'Город', 'Прочая информация'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['city'], item['info']])


def parse():
    URL = input('Введите ссылку: ')
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'page' : page})
            cars.extend(get_content(html.text))
            save_file(cars, FILE)
        print(f'Получено {len(cars)} автомобилей')
        os.startfile(FILE)
    else:
        print('Error')

parse()
