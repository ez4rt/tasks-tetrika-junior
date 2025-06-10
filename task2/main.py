import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import csv


def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        return None


def parse_page(html_content, animal_count):
    soup = BeautifulSoup(html_content, "html.parser")
    animal_links = soup.select('div.mw-category-group ul li a[title]')

    for link in animal_links:
        title = link['title']
        if 'Категория:' not in title:
            first_letter = title[0].upper()
            animal_count[first_letter] += 1

    next_page_link = soup.find('a', text='Следующая страница')
    if next_page_link:
        return f"https://ru.m.wikipedia.org{next_page_link['href']}"
    return None


def save_to_csv(data):
    with open('beasts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for key, value in data.items():
            writer.writerow([key, value])


def main():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    animal_count = defaultdict(int)

    while url:
        html_content = fetch_html(url)
        if html_content:
            url = parse_page(html_content, animal_count)
        else:
            break

    animal_count = dict(sorted(animal_count.items()))
    print(animal_count)
    save_to_csv(animal_count)


if __name__ == "__main__":
    main()