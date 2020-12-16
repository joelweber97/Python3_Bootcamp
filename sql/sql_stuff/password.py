#SQL Injection

import sqlite3
conn = sqlite3.connect('users.db')

# query = "CREATE TABLE users (username TEXT, password TEXT);"

u = input('Please enter your username: ')
p = input('Please enter your password: ')

#if a person types ' OR 1 = 1 -- as their password it will always log in
#creates the query f"SELECT * FROM users WHERE username = 'username' AND password = '' OR 1 = 1 --'"
#which is always true
c = conn.cursor()
query = f"SELECT * FROM users where username = '{u}' AND password = '{p}'"
c.execute(query)

#better to use question marks and input the u and p as a tuple
c = conn.cursor()
query = f"SELECT * FROM users WHERE username = ? AND password = ?"
c.execute(query, (u, p))

result = c.fetchone()
if(result):
    print('welcome back')
else:
    print('failed login')
conn.commit()
conn.close()