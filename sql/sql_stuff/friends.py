import sqlite3

'''
##### Connecting to a db and creating a table #######
conn = sqlite3.connect('my_friends.db')
#create cursor
c = conn.cursor()
#execute some sql
c.execute('CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);')
#commit changes
conn.commit()
#close the connection
conn.close()
'''

'''
##### Inserting into the table we created above ######
#wouldnt really use it this way becuase the values are static
#would only use python of the values change 
#maybe a bunch of stuff in a csv file that you want in the db
#connect to the db
conn = sqlite3.connect('my_friends.db')
#create cursor
c = conn.cursor()
#execute some sql
insert_query = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)"
c.execute(insert_query)
#commit changes
conn.commit()
#close the connection
conn.close()
'''

'''
#if we have a bunch of variable that need to be added
conn = sqlite3.connect('my_friends.db')
#create cursor
c = conn.cursor()
#execute some sql
form_first = "Mary-Todd"
query = "INSERT INTO friends (first_name) VALUES (?)"   #the question mark is used as a variable place holder
c.execute(query, (form_first,))   #form_first is a tuple so it needs parens and a comma if only 1 entry
#commit changes
conn.commit()
#close the connection
conn.close()
'''

#if we have a bunch of variable that need to be added
conn = sqlite3.connect('my_friends.db')
#create cursor
c = conn.cursor()
#execute some sql
data = ('Steve', 'Irwin', 9)    #tuple of data
query = "INSERT INTO friends VALUES (?, ?, ?)"   #the question marks are used as a variable place holder
c.execute(query, data)   #the data variable is a tuple so we don't need parens around it this time
#commit changes
conn.commit()
#close the connection
conn.close()




