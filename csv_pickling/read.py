# with open('fighters.csv') as file:
    # f = file.read()
   
# print(f)
#this method returns one giant string so its not easy to work with at all
#difficult to parse correctly


print('######### CSV READER ############')
from csv import reader
with open('fighters.csv') as file:
    csv_reader = reader(file)
    for fighter in csv_reader:
        #each row is a list
        print(fighter)
        print(f'{fighter[0]} is from {fighter[1]}')
        

#if we don't want the header in the print out we can use next() like we did in the iterator section
with open('fighters.csv') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(fighter)
        
#we can also save the reader as a list so when the reader object closes we can still have access to the data

with open('fighters.csv') as file:
    csv_reader = reader(file)
    #csv_reader isnt a list, its an iterator
    data = list(csv_reader)
    #data is now a list of lists
print(data)



print('########## DictReader #############')
from csv import DictReader
with open('fighters.csv') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        #each row is an OrderedDict
        print(row)
        
        
#rather than using the index values like we did for reader()
#we can just use the dict key to access the data
with open('fighters.csv') as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row['Name'])