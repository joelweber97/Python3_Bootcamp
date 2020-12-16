class Human:
    def __init__(self, first,last,age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f" Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    #__add__ will take two humans add them together to create a new human that's zero years old.
    def __add__(self, other): #self is the first person, other is the second person.
        #small check to make sure other is a Human
        if  isinstance(other, Human):
            return Human(first = 'newborn', last = self.last, age = 0) #since self is the first person (j) the last name will automatically be taken from the first person (larson)
        return 'you cannot add that'


    def __mul__(self, other):  #cloning humans #self refers to the first operand.
        if isinstance(other, int):
            return [self for i in range(other)]  #returns self (j, in our case) for every value in the range of other. #returns a list containing Human __repr__ that is other in length
        return 'Cannot muliply'


j = Human("jenny", 'Larson', 47)
print(j)  #'Human named jenny larson'
print(len(j))  #we defined __len__ to return the age of the human
#if we didnt define what __len__ was above, calling len(j) would thrown an error

k = Human('kevin', 'jones', 49) #creating the second human

#adding j + k returns Human(first = 'newborn', last = self.last, age = 0) #since self is the first person (j) the last name will automatically be taken from the first person (larson)
print(j+k)   #printing this will return the __repr__ string of the __add__ method
#Human named newbord larson


print(j*2)  #uses the __mul__ method   #[Human name jenny larson aged 47, Human named jenny larson aged 47]


triplets = j * 3
triplets[1].first = 'jessica'   #changing the second triplet to have the name jessica
print(triplets)  #they all say jessica   #they all changed because all 3 triplets are the exact same object. #making a change to 1 makes changes to all of them.


'''
we can make each one a differet object we can import copy
and use that to make separate copies of each of the three
from copy import copy
def __mul__(self,other):
  return [copy)self fo ri in range(other)]

j = Human('Jenny', 'Larson', 47)
triplets = j * 3    # [human named jenny larson aged 47, human named jenny larson aged 47, human named jenny larson aged 47]
triplets[1].first = 'Jessica'  #[human named jenny larson aged 47, human named jessica larson aged 47, human named jenny larson aged 47]


(k+j) * 3  #newborn jones aged 0 * 3



'''