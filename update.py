import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor()
    print("before updating a recorde")
    str="""select * from student where rollno=100"""
    cur.execute(str)
    rec=cur.fetchone()
    print(rec)
    #update single record
    str1=""" update student set sname='ritu' where rollno=100"""
    cur.execute(str1)
    con.commit()
    print("recorde updated successfully")
    print("after updating record")
    cur.execute(str1)
    rec=cur.fetchone()
    print(rec)
except mysql.connector.Error as e:
    print("failed to update recorde {}".format(e))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("connection is close")
