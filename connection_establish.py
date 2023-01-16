import mysql.connector
from mysql.connector import Error
#import error from mysql.connector

try:
    con=mysql.connector.connect(host='localhost', database='mymca', user='root', password='manisha')
    if con.is_connected():
        db_info=con.get_server_info()
        print("connection to mysql server version",db_info)
        cur=con.cursor()
        cur.execute("select database();")
        record=cur.fetchone()
        print("you are connected to  database",record)
except Error as e:
    print("Error while connecting to mysql",e)
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("mysql connection is closed")