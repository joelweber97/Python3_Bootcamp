class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species
        
    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f'You cannot have a {species} as a pet')
        self.species = species
            
            
cat = Pet('Blue', 'cat')
print(cat.name, cat.species)
dog = Pet('Wyatt', 'dog')
print(dog.name, dog.species)
# tiger = Pet('Fluffy', 'tiger')

print(cat.species)
#cat.set_species('tiger') #will throw a value error
cat.set_species('rat')
print(cat.species)


#can alter the allowed species list just by changing the class attribute vs
#having to change all the allowed this for every instance.
Pet.allowed.append('pig')
print(Pet.allowed)
print(cat.species)
cat.set_species('pig')
print(cat.species)
