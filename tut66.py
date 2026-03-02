import sqlite3
conn = sqlite3.connect("sqlite3.db")
# conn.execute('''
#  CREATE TABLE IF NOT EXISTS fees(
#     st_id int auto primary key,
#     st_fee VARCHAR(5),
#     st_email VARCHAR(20)
#  );
#  ''')
# data = " insert INTO fees(st_id,st_fee,st_email) VALUES('4','6000','belafon@gmail')"
# conn.execute(data)
# conn.commit()
data= conn.execute("SELECT * FROM tb2")
for a in data:
    print(a)
print("\n") 
data= conn.execute("SELECT * FROM fees")
for a in data:
    print(a)
# conn.close()

print("\n") 
data= conn.execute("SELECT * FROM fees as f inner join tb2 as t on f.ab_id=t.ab_id")
for a in data:
    print(a)
conn.close()
# print('\n')
# st_name=input(" enter name for sarche :-  ")
# # data = conn.execute("SELECT * FROM tb2 where ab_name='"+st_name+"'")
# data = conn.execute("SELECT * FROM tb2 where ab_name like'%"+st_name+"%'")
# for a in data:
#     print(a)
