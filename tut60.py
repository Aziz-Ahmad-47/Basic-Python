import sqlite3
con=sqlite3.connect("sqlite1.db")
con.execute('''
   Table (
    st_name VARCHAR(20)
    st_id VARCHAR(20)
    st_roll VARCHAR(20)
    )

''')
con.close()