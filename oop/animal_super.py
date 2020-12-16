class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def __repr__(self):
        return f"{self.name} is a {self.species}"
        
    def make_sound(self, sound):
        print(f"This animal says {sound}")
        
    
class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        super().__init__(name,species)
        self.breed = breed
        self.toy = toy
    def play(self):
        print(f"{self.name} playes with {self.toy}")
        
        
c = Cat('blue', 'cat', 'tabby', 'string')
print(c)