'''
from csv import reader, writer
#read the data from 1 csv file and write it to another
#csv file in all caps
with open('fighters.csv') as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]

        
#now all we have to do is take the fighters list and write it to the new file        
with open('screaming_fighters.csv', 'w', newline = '') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)
''' 
    
# can also next all of these lines together
#the csv writer has to be nested otherwise the fighters.csv file will close
#and wont be used for the writerow.
from csv import reader, writer
with open('fighters.csv') as file:
    csv_reader = reader(file)
    with open('screaming_fighters.csv', 'w', newline = '') as file2:
        csv_writer = writer(file2)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])
            
#above isn't necessarily a good approach if you are leaving a bunch of files open.
#generally we want to close files as soon as we have what we need out of them.
