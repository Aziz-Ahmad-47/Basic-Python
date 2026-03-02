import sqlite3
conn= sqlite3.connect("sqlite2.dp")

inn='''
    insert into student (st-name, st-class, st-email) VALUES('aziz','13',"gmail.com")
    '''
conn.execute(inn)
conn.commit()
conn.close()