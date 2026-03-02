import sqlite3
con = sqlite3.connect("sqlite.db")
con.execute('''
     CREATE TABLE IF NOT EXISTS todo(
          st_id int auto primary key,
          st_name VARCHAR(50),
          st_class VARCHAR(50),
          st_email VARCHAR(50)
          );
 ''')
# con.close()

ins = " INSERT INTO todo(st_id,st_name, st_class, st_email) VALUES('2','sana','13','gmail.com');"
con.execute(ins)
con.commit()
con.close()