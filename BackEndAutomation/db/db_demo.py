import mysql.connector
from utilities.configurations import *

# $ pip install mysql-connector-python

# host, database, user, password
# connection = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='mysql1234')
connection = get_connection()
print(connection.is_connected())
cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')

# row = cursor.fetchone()     # fetch the very first row in the table
# print(row)
# print(row[3])
# row = cursor.fetchone()     # Now cursor is looking to the next row in the table
# print(row)
# rows = cursor.fetchall()    # fetchall remaining rows
# print(rows)
# print(rows[1][3])

sum_amount = 0
rows = cursor.fetchall()
print(rows)
for row in rows:
    # print(row[2])
    sum_amount += row[2]

print(sum_amount)
assert sum_amount == 340

query_to_update = "Update CustomerInfo set Location = %s where CourseName = %s"
data = ('BR', 'Jmeter')
cursor.execute(query_to_update, data)
connection.commit()
# print(rows)

for row in rows:
    if row[0] == 'Jmeter':
        print(row)

query_to_insert = "INSERT INTO CustomerInfo values('Devops', CURRENT_DATE(), '80', 'South America')"
# insert_date = ('Devops', , '80', 'South America')
cursor.execute(query_to_insert)
connection.commit()
# rows2 = cursor.fetchall()
# print(rows2)

query_to_delete = "delete from CustomerInfo where CourseName = %s"
delete_data = ('Devops',)
cursor.execute(query_to_delete, delete_data)
connection.commit()

# cursor = connection.cursor()
# rows = cursor.fetchall()
# print(rows)

connection.close()
