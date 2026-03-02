import sqlite3
tab=sqlite3.connect('sqlite1.db')

tab.execute('''
  CREATE TABLE IF NOT EXISTS student(
    ab_name VARCHAR(20),
    ab_saction VARCHAR(30),
    ab_year VARCHAR(30)
  );
''')
inn="INSERT INTO student(ab_name,ab_saction,ab_year) VALUES('aziz', 'B','2021-25')"
inn="INSERT INTO student(ab_name,ab_saction,ab_year) VALUES('ahmad', 'A','2022-26')"
# inn="INSERT INTO student(ab_name,ab_saction,ab_year) VALUES('Khasman', 'C','2023-27')"
tab.execute(inn)
tab.commit()
tab.close()