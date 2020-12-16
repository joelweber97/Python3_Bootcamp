class A:
    def do_something(self):
        print('Method Define In: A')

class B(A):
    def do_something(self):
        print('Method Define In: B')

class C(A):
    def do_something(self):
        print('Method Define In: C')
        
class D(B,C):
    pass


#     A
#   /   \
#  B     C
#    \  /
#     D
#B and C both inherit from A
#D inherits from both B and C


#to find out which of the classes will be run first we pull up the mro
print(D.__mro__) 
print(D.mro())
print(help(D))
#the order of D, B, C, A 


thing = D()
thing.do_something() #prints method defined in B since that was the first one in the order with anything in it.
#if we had a print statement in D, it would have run instead of what was in B
#if nothing was in D and B, C would have run.


#when super.__init__ is defined in a class it is actually calling the next class in the MRO order.
 