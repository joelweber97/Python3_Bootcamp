from csv import writer
with open('cats.csv', 'w', newline = '') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Name', 'Age'])
    csv_writer.writerow(['Blue', 3])
    csv_writer.writerow(['Kitty', 1])




from csv import DictWriter
with open('cats.csv', 'w', newline = '') as file:
    headers = ['Name', 'Breed', 'Age']
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader() #at this point the headers will be written to the file
    csv_writer.writerow({'Name': 'Garfield', 'Breed': 'Orange Tabby', 'Age': 10})
    