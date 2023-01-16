import mysql.connector
try:

    con=mysql.connector.connect(host='localhost',
                            database='mymca',
                            user='root',
                            password='manisha')
    str="select * from student"
    cur=con.cursor()
    cur.execute(str)
    rec=cur.fetchall()
    print("total no of rows in table",cur.rowcount)
    print("printing each row")
    for r in rec:
        print("rollno:-",r[0])
        print("name:-",r[1])
        print("class:-",r[2])
        print("marks:-",r[3],"/n")
except mysql.connector.Error as e:
    print('error is:-',e)
finally:

    if con.is_connected():
        con.close()
        cur.close()
        print("connection closed")