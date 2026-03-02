import sqlite3
conn = sqlite3.connect("sqlite2.db")
data = conn.execute("SELECT * FROM tb1")
print("tb1 st_id","tb1 st_name","tb1 st_rollno","tb1 st_class")
for n in data:
    print(n[0],n[1],n[2],n[3])