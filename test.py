import mysql.connector
try:
    connection=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha0288')
    if connection.is_connected():
        db_info=connection.get_server_info()
        print("connection to MYSQL server version",db_info)
        cursor=connection.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("you`re connected to database record")
except mysql.connector.Error  as e:
    print("Error reading data from mysql table",e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MYSQL connection is used")