import requests as r
from csv import writer, DictReader
from bs4 import BeautifulSoup as bs
from random import choice


BASE_URL = 'http://quotes.toscrape.com'

def read_quotes(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)
        
     

def start_game(quotes):
    quote = choice(quotes)
    print('Here is a quote: ')
    print(quote['text']) 
    remaining_guesses = 4
    guess = ''
    # print(quote['author'])
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

quotes = read_quotes('quotes.csv') 
# quotes = scrape_quotes()
start_game(quotes)