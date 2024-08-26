import sqlite3

dbase = sqlite3.connect('Our_data.db')
print('Database opened')

# Drop the existing table if it exists
dbase.execute('''DROP TABLE IF EXISTS employee_records''')
print('Existing table dropped')

# Create a new table with the correct schema
dbase.execute('''CREATE TABLE employee_records(
       ID INT PRIMARY KEY NOT NULL,
       NAME TEXT NOT NULL,
       DIVISION TEXT NOT NULL,
       STARS INT NOT NULL)''')
print('Table created')

# Insert multiple records at once
dbase.execute('''INSERT INTO employee_records(ID,NAME,DIVISION,STARS) 
                 VALUES(1,'Lenny','software',3),
                        (2,'Monkey','Programmer',5)''')

dbase.commit()

dbase.close()
print('Database closed')
