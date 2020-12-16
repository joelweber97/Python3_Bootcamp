from csv import DictReader, DictWriter

def cm_to_in(cm):
    return cm * 0.393701
    
with open('fighters.csv') as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)
    
with open('inches_fighters.csv', 'w', newline = '') as file:
    csv_writer = DictWriter(file, fieldnames = ['Name', 'Country', 'Height(in)'])
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
        'Name': f['Name'], 'Country': f['Country'], 'Height(in)': cm_to_in(float(f['Height (in cm)']))})
    