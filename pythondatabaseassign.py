import sqlite3

conn = sqlite3.connect('databaseassign.db')

with conn:
    cur = conn.cursor()
    cur.execute("create table if not exists tbl_filename(\
    ID integer primary key autoincrement,\
    col_file text)")

    conn.commit()
conn.close()

conn = sqlite3.connect('databaseassign.db')
with conn:
    cur = conn.cursor()
    cur.execute("insert into tbl_filename(col_file) values (?)", ('information.docx',))             
    cur.execute("insert into tbl_filename(col_file) values (?)", ('hello.txt',))
                
    cur.execute("insert into tbl_filename(col_file) values (?)", ('myimage.png',))
                
    cur.execute("insert into tbl_filename(col_file) values (?)", ('mymovie.png',))
                
    cur.execute("insert into tbl_filename(col_file) values (?)", ('world.txt',))
                
    cur.execute("insert into tbl_filename(col_file) values (?)", ('data.pdf',))
                
    cur.execute("insert into tbl_filename(col_file) values (?)", ('myphoto.jpg',))     
    conn.commit()
conn.close()

conn = sqlite3.connect('databaseassign.db')
with conn:
    cur = conn.cursor()
    cur.execute("select col_file from tbl_filename where col_file like '%.txt'")
    txtfilelist = cur.fetchall()
    for item in txtfilelist:
        txtfilelist = "File Name ending with: {}".format(item[0])
        print(txtfilelist)
conn.close()


