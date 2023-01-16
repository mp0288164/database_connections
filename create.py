import mysql.connector
try:
    connection=mysql.connector.connect(host='localhost',
                                        database='mymca',
                                        user='root',
                                        password='manisha')
    query="""CREATE TABLE employee2(id varchar(10),name varchar(20),joining_date int,salary int(5) Not Null,PRIMARY KEY(id))"""
    cursor=connection.cursor()
    cursor.execute(query)
    print("employee table created successfully")
except mysql.connector.Error as e:
    print("Failed to create table in mysql:-{}".format(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("mysql connection is closed")
        

                