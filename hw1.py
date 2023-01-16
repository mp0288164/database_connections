import mysql.connector
try:
    conn=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    myc="""CREATE TABLE employee1(empid varchar(20) PRIMARY KEY,empname varchar(35),empsalary int(6) Not Null)"""
    cur=conn.cursor()
    cur.execute(myc)
    print("employee1 table created successfully")
except mysql.connector.Error as e:
    print("failed to create table in mysql:-{}".format(e))
finally:
    if conn.is_connected():
        cur.close()
        conn.close()
        print("mysql cinnection is closed")