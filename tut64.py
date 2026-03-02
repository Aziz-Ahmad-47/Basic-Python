import sqlite3
conn=sqlite3.connect("sqlite2.db")
st_id=input("enter the id for delete")
conn.execute("DELETE FROM tb1 where st_id="+st_id)
conn.commit()
conn.close()