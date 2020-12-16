import requests as r
from csv import writer
from bs4 import BeautifulSoup as bs
from random import choice
from time import sleep
from csv import DictWriter

BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        response = r.get(f'{BASE_URL}{url}')
        response.encoding = 'utf-8'
        print(f'Now scarping {BASE_URL}{url}')
        soup = bs(response.text, 'html.parser')
        # print(soup)
        
        quotes = soup.find_all(class_ = 'quote')

        for q in quotes:
            all_quotes.append({'text': q.find(class_ = 'text').get_text(), 
            'author': q.find(class_ = 'author').get_text(),
            'bio_link': q.find('a')['href']})

        next_btn = soup.find(class_ = 'next')
        url = next_btn.find('a')['href'] if next_btn else None
        #waits 2 seconds between scrapes so we don't attract attention.
        # sleep(2)
    return all_quotes

def write_quotes(quotes):
    with open('quotes.csv', 'w', encoding='utf-8', newline='') as file:
        headers = ['text', 'author', 'bio_link']
        csv_writer = DictWriter(file, fieldnames = headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)
    
quotes = scrape_quotes()
write_quotes(quotes)