
'''
from csv import writer
def add_user(first, last):
	with open('users.csv', 'a') as file:
		csv_writer = writer(file)
		csv_writer.writerow([first, last])
        
        
add_user('Dwayne', 'Johnson')
'''

'''
import csv
def print_user():
    with open('users.csv') as csvfile:
        csv_reader =csv.DictReader(csvfile)
        for row in csv_reader:
            print('{} {}'.format(row['First Name'], row['Last Name']))


print(print_user())
'''


    
    