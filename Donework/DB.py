import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="945295AZielp",
  database="kodjodb"
)

print("Db Details: ",mydb)

# 9mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print("List of Db: ",x)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM shop_items")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)