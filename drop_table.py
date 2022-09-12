import mysql.connector

conn = mysql.connector.connect(user='root', password='abc123',host='127.0.0.1',database='mysql')

cursor = conn.cursor()
cursor.execute("SHOW Tables")
print(cursor.fetchall())

cursor.execute("DROP TABLES EMPLOYEE")
print("Table dropped... ")
conn.commit()

print("List of tables after dropping the EMPLOYEE tables: ")
cursor.execute("SHOW Tables")
print(cursor.fetchall())
conn.close()