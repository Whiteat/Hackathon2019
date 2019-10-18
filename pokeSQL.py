import mysql.connector
from mysql.connector import Error

try:
    ## Your going to have to figure out how to enter my IP address
    ## Users (alex,corey,jon,josh) passwords: (H@ckath0n or H@ckaj0n)
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='jon',
                                         password='H@ckaj0n')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
