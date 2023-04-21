import sqlite3

with sqlite3.connect("roster.db") as connection:
    c = connection.cursor()
    c.executescript("""drop table if exists roster;
              create table roster(name text, species text, IQ int);
              insert into roster values('ron','obvious','42');""")

rostervalues = (('Jean-Baptiste Zorg', 'human', 122),\
                ('Korben Dallas', 'Meat Popsicle', 100),\
                ('Ak\'not', 'Mangalore', -5))
c.executemany("insert into roster values(?,?,?)", rostervalues)
c.execute("update roster set species=? where name=? and IQ=?",\
          ('human', 'Korben Dallas', 100))
c.execute("select name, IQ from roster where species = 'human'")

while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)
