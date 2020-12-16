class Animal:
    cool = True
    def make_sound(self, sound):
        print(f"this animal says {sound}")



class Cat(Animal):
    pass
    
    
    
a = Animal()
print(a)
a.make_sound('woof')
print(a.cool)


c = Cat()
print(c)
c.make_sound('meow')
print(c.cool)
print(Cat.cool)