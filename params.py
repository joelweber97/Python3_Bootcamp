import requests
#changed url to include /search
url = 'https://icanhazdadjoke.com/search'

response2 = requests.get(url, 
                headers= {'Accept': 'application/json'},
                params = {'term': 'cat','limit': 1})

data = response2.json()

#print(data['joke'])
#print(f"Status: {data['status']}")
print(data)
#data gives us a json file containing page info
#and results of the search.
#the results are a list of jokes in a dict with and id and the joke
print(data['results'])