import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect('example.db') as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute('CREATE TABLE if not Exists posts(title TEXT, details TEXT)')

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Great", "I\'m great.")')
    c.execute('INSERT INTO posts VALUES("India", "I\'m from India.")')
