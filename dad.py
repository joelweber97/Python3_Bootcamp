import random
from pyfiglet import figlet_format
import requests as r
from colorama import init
from termcolor import colored

# use colorama to make termcolor work on Windows too
init()
#dad joke banner
print(colored(figlet_format('Dad Joke 3000', font='slant'), color='magenta'))

#get a topic from the user
topic = input('Let me tell you a joke! Give me a topic: ')

#url to search the values
url = 'https://icanhazdadjoke.com/search'

#run the get response with appropriate headers and params
response = r.get(url, 
    headers = {'Accept':'application/json'}, 
    params = {'term': topic}).json()
    
results = response['results']
#print(results)
'''
##################option 1#######################
if len(results) == 1:
    print(results['joke'])
elif len(results) > 1:
    print(random.choice(results)['joke'])
else:
    print(f'There are not jokes pertaining to {topic}')
'''

################option 2##############################
num_jokes = response['total_jokes']
#print(num_jokes)
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {topic}")
    print(random.choice(results)['joke'])
elif num_jokes == 1:
    print(f"There is only 1 joke about {topic}")
    print(results[0]['joke'])
else:
    print(f'There are not jokes about {topic}')


