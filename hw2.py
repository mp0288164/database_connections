import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    mya="""ALTER TABLE employee1 add company_name varchar(20) Not Null"""
    cur=con.cursor()
    cur.execute(mya)
    print("successfully added new coloum in employee1 table")
except mysql.connector.Error as e:
    print("Failed to added new coloum in employee1 table")
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("connection is closed")