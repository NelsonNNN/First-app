import sqlite3

with sqlite3.connect('welcomes.db') as connection:
    c = connection.cursor()
    c.execute('CREATE TABLE table3(title TEXT, description TEXT)')
    c.execute('INSERT INTO TABLE table3 VALUES("If you are a gamer", "click here")')
    c.execute('INSERT INTO TABLE table3 VALUES("If you are a guitarist", "Click here")')