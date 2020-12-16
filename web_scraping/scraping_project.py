import requests as r
from csv import writer
from bs4 import BeautifulSoup as bs
from random import choice
from time import sleep

BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        response = r.get(f'{BASE_URL}{url}')
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
        

def start_game(quotes):
    quote = choice(quotes)
    print('Here is a quote: ')
    print(quote['text']) 
    remaining_guesses = 4
    guess = ''
    print(quote['author'])
    while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
        guess = input(f'Guess who wrote that quote: ({remaining_guesses} guesses remaining)\n')
        remaining_guesses -= 1
        if guess.lower() == quote['author'].lower():
            print('You got it right')
            break
        if remaining_guesses == 3:
            #hint of the person's bday and birth location
            res = r.get(f"{BASE_URL}{quote['bio_link']}")
            soup = bs(res.text, 'html.parser')
            birth_date = soup.find(class_ = 'author-born-date').get_text()
            birth_location = soup.find(class_ = 'author-born-location').get_text()
            print(f"This person was born on {birth_date} {birth_location}")
        elif remaining_guesses == 2:
            #hint of the authors first initial
            first_initial = quote['author'][0].upper() 
            print(f"Peron's first name starts with {first_initial}. ")
        elif remaining_guesses == 1:
            last_intial = quote['author'].split(' ')[1][0].upper()
            print(f"Person's last name starts with {last_intial}.")
        else:
            print(f"Sorry you ran out of guesses. The correct answer was {quote['author']}.")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input('Would you like to play again? (y/n) ')
    if again.lower() in ('y', 'yes'):
        print('ok you are playing again')
        return start_game(quotes)
    else:
        print('goodbye')

quotes = scrape_quotes()
start_game(quotes)