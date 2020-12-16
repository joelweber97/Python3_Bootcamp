import requests

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers = {'Accept': 'text/plain'})
response2 = requests.get(url, headers= {'Accept': 'application/json'})

#print(response.text)


print(response2.text)
print(response2.json())

data = response2.json()

print(data['joke'])