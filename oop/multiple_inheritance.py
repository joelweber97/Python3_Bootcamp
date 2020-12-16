
class Aquatic:
    def __init__(self, name):
        print('Aquatic init')
        self.name = name
        
    
    def swim(self):
        return f"{self.name} is swimming"
  
    def greet(self):
        return f"I am {self.name} of the sea"
   
class Ambulatory:
    def __init__(self,name):
        print('Ambulatory Init')
        self.name = name
        
   
    def walk(self):
        return f"{self.name} is walking"
 
    def greet(self):
        return f"I am {self.name} of the land"

#penguin has all of the methods from aquatic and ambulatory
#aquatic and ambulatory are in no way connected to each other

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print('Penguin Init')
        super().__init__(name = name)



print('##############')
jaws = Aquatic('Jaws')
lassie = Ambulatory('Lassie')
captain_cook = Penguin('Captain Cook')
print('##############')
#pulls the walk method from ambulatory
print(captain_cook.walk())
#pulls the swim method from aquatic
print(captain_cook.swim())
#pulls greet method from ambulatory, but not from Aquatic
print(captain_cook.greet())
print('##############')
#captain_cook is an instance of Penguin, Aquatic, and Ambulatory so how does the line above know which .greet() to use?
print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")
print('##############')
captain_cook = Penguin('Captain Cook')
#When we had print statements to each method we can see the order in which they are processed.
#1 - Penguin init
#2 - Ambulatory init
#this is based off the order in which the methods are used as arguments in Penguin
#in this case Penguin(ambulatory, aquatic) ambulatory is first so it gets run when printing captain_cook.speak()
# if we switched it to class Penguin(Aquatic, Ambulatory) and ran penguin.speak() it would print the aquatic version
print('##############')
#we can add Aquatic.__init__(self, name = name) under super().__init__ to activate the aquatic init as well.
class Penguin2(Ambulatory, Aquatic):
    def __init__(self, name):
        print('Penguin 2 init')
        super().__init__(name = name)
        Aquatic.__init__(self, name = name)

captain_cook2 = Penguin2('Captain Cook')
#this prints all three init print statements whereas only Penguin and Ambulatory were printed before
print('##############')
#If calling both it's better to be specific so we should use the following instaed of super()
class Penguin3(Ambulatory, Aquatic):
    def __init__(self, name):
        print('Penguin 3 init')
        Ambulatory.__init__(self, name = name)
        Aquatic.__init__(self, name = name)
captain_cook3 = Penguin3('Captain Cook')

print('###############')
#There are 3 ways to access the order of method resolution
# 1- using the __mro__ attribute on the class
print(Penguin3.__mro__)
# 2- using the mro() method on the class
print(Penguin3.mro())
# 3- use the built in help(cls) method
print(help(Penguin3))