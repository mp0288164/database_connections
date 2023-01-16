import mysql.connector
try:
    connection=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    mysql_insert_query="""INSERT INTO employee(empid,empname,empsalary)VALUES('E001','manisha',70000)"""
    cursor=connection.cursor()
    cursor.execute(mysql_insert_query)
    connection.commit()
    print(cursor.rowcount,"Record inserted successfully into employee table")
except mysql.connector.Error as error:
    print("Failed to insert record into employee table{}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MYSQL connection is closed")
