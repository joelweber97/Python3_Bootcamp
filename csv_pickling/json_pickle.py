import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat('Charles', 'Tabby')
with open('cat.json', 'w') as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)  
#this creates a new json file with the following printed in items
#{"py/object": "__main__.Cat", "name": "Charles", "breed": "Tabby"}

#to read in a json pickle we use the following code
import jsonpickle
class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
with open('cat.json', 'r') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)
    print(unfrozen.name)
