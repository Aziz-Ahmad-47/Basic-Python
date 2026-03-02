import sqlite3
conn=sqlite3.connect("sqlite2.db")
conn.execute('''
   update tb1 set st_id='1' where st_id=2
''')
conn.commit()
conn.close()