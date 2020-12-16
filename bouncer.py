# as for age
#18-21 wrist band
#21 + you can drink
#otherwide you're too young.


age = input('Enter your age: ')

'''
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print('you can enter but need a wrist band')
    elif age >= 21:
        print('you can enter and drink')
    else:
        print('you cannot enter')
else:
    print('please enter an age')
'''

if age:
    age = int(age)
    if age >= 21:
        print('you can drink')
    elif age >= 18:
        print('you can enter with a wristband')
    else:
        print('you cant enter')
else:
    print('please enter an age')
        