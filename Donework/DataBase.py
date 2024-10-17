# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="945295AZielp",
#   database="kodjodb"
# )

# print("Db Details: ",mydb)

# # 9mycursor = mydb.cursor()

# # mycursor.execute("SHOW DATABASES")

# # for x in mycursor:
# #   print("List of Db: ",x)

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM shop_items")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

import mysql.connector
import DBscripts
name=str(input("Enter your Name "))
age=int(input("Enter your Age "))

def Database():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="945295AZielp",
    database="kodjodb"
    )
    mycursor=mydb.cursor()
    mycursor.execute(f"INSERT INTO notebook (PersonID,Personname ,Personage) VALUES (1, '{name}', '{age}')")
    # mycursor.execute(f"SELECT * FROM notebook where PersonID = '2'")
    # mycursor.execute(DBscripts.InsertPersons(a=1,b=name,c=age))
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
Database()

