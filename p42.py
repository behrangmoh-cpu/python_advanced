import sqlite3
con = sqlite3.connect("db2.db")
cur = con.cursor()
code=int(input("Enter code : "))
name=input("Enter new name : ")
family=input("Enter new family : ")
res = cur.execute(f"update personal set fname='{name}',lname='{family}' where code={code}")
con.commit()