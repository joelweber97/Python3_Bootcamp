#defining the simplest possible class

class User:
    active_users = 0
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
        
    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
    def __repr__(self):
        return f"{self.first} is {self.age}"
        
    def logout(self):
        User.active_users -+ 1
        return f"{self.first} has logged out"
    def full_name(self):
        return f"{self.first} {self.last}"
        
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
        
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
        
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"
        
        
user1 = User('Joe', 'Smith', 68)
user2 = User('Blanca', 'Lopez', 41)


#print(user1.first, user1.last)
#print(user2.first, user1.last)
# print(user2.full_name())
# print(user1.initials())
# print(user1.likes('fuit'))
# print(user2.is_senior())
# print(user1.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# print(user2.age)
# print(user2.birthday())
# print(user2.age)


# print(User.active_users)
# user1 = User('Joe', 'Smith', 68)
# user2 = User('Blanca', 'Lopez', 41)
# print(User.active_users)
# print(user1.logout())
# print(User.active_users)


# print(User.display_active_users())
# user3 = User('John', 'Smith', 16)
# user4 = User('Bianca', 'Lopez', 32)
# print(User.display_active_users())

#User('Sue, Pritchet, 12') # this syntax wont work so we can use a class method to convert this format to a format we can take into the class.
tom = User.from_string('Tom,Jones,89')  #This should be able to be read into an instance
# print(tom.first)
# print(tom.full_name())
# print(tom.birthday())

print(tom)  #this would usually just print out <__main__.User object at mem space>
#but with __repr__ method we made above we can actually control what is printed out when we print the user1


j = User('Judy', 'Steel', 18)
j = str(j)   #this works to turn the <__main__.User object> output into a normal string as well.
print(j)
