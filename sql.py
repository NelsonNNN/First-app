import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('trial.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute('CREATE TABLE titles(title TEXT, details TEXT)')

    # insert dummy data into the table
    c.execute('INSERT INTO titles VALUES("Name", "Nelson.")')
    c.execute('INSERT INTO titles VALUES("Age", "24 years.")')
    c.execute('INSERT INTO titles VALUES("Likes", "Guitar.")')
    c.execute('INSERT INTO titles VALUES("Ambitions", "to join Andela.")')