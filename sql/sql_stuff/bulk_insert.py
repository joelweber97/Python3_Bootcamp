import sqlite3

conn = sqlite3.connect('my_friends.db')

c = conn.cursor()

#using a list of tuples
people = [
    ('Ronald', 'Amundsen', 5),
    ('Rosa', 'Parks', 8),
    ('Henry', 'Hudson', 7),
    ('Neil', 'Armstrong', 7),
    ('Daniel', 'Boone', 3)]
 
#c.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)  #takes a list of tuples(people) and runs the insert command on each person
 
# one option is iterating over people
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print("INSERTING NOW!")
    

#for loop works best if you want to do other stuff besides just a bulk add
closeness = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    closeness += person[2]
print(closeness/len(people))
    




conn.commit()
conn.close()