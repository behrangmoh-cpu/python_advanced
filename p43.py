import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)
cur=connection.cursor()
myquery=f'''select * from t1'''
cur.execute(myquery)
rows=cur.fetchall()
for row in rows:
    print(f"{row[0]:<10}{row[1]:<20}{row[2]:<20}{row[3]:<20}")
code = int(input("select id : "))
new_name=input("Enter name for update : ")
new_family=input("Enter family for update : ")
new_age=int(input("Enter age for update : "))
myquery_update=f'''update t1
                    set name='{new_name}',family='{new_family}',age={new_age}
                    where code={code}'''
try:
    cur.execute(myquery_update)
except:
    print("not found")
connection.commit()