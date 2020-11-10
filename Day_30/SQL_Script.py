import mysql.connector


my_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql',
    'database': 'testdb',
}

mycursor = mysql.connector.connect(**my_config)

mycursor.execute("Select * FROM firsttable")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
