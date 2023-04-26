import sqlite3

with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    c.executescript("""drop table if exists people;
              create table people(firstname text, lastname text, age int);
              insert into people values('ron','obvious','42');""")

peoplevalues = (('luigi', 'verocottie', 43), ('arthur', 'belling', 28))
c.executemany("insert into people values(?,?,?)", peoplevalues)
    
