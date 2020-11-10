import mysql.connector


def mysql_Connect():
    my_config = {
        'host': 'localhost',
        'port': '3306',
        'user': 'root',
        'password': 'mysql',
        'database': 'testdb',
    }
    cnx = mysql.connector.connect(**my_config)

    return cnx
