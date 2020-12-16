import sqlite3
#connect to the db
conn = sqlite3.connect('my_friends.db')
#create the cursor
c = conn.cursor()
#select all friends in the db
# c.execute("SELECT * FROM friends")
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

#can grab the first instance in the table
print('###### c.fetchone() ######')
print(c.fetchone())   

print('###### c.fetchall() #######')
# c.execute("SELECT * FROM friends")
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
#can also fetch everything and save it as a list of tuples
print(c.fetchall())

print('#######Iterate over the cursor#####')
# c.execute("SELECT * FROM friends")
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")
for result in c:
    print(result)

  
#commit changes
conn.commit()
#close the db connection
conn.close()