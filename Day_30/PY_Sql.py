import sys
import DB_Connect
try:
    db_cnx = DB_Connect.mysql_Connect()
    cursor = db_cnx.cursor()

    my_query = "Select * FROM firsttable"
    cursor.execute(my_query)

    result = cursor.fetchall()
    print(result)
except Exception as e:
    print(e)

finally:
    cursor.close()
    db_cnx.close()
