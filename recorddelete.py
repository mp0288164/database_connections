import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor()
    print("student table before deleting")
    str="""SELECT * from student where rollno=100"""
    cur.execute(str)
    rec=cur.fetchone()
    print(rec)
     #delect recorde
    str1="""DELETE FROM  student where rollno=100"""
    cur.execute(str)
    con.commit()
    print(cur.rowcount,"no of recorde deleted successfully")
    # check record
    cur.execute(str)
    rec1=cur.fetchall()
    if len(rec)==0:
        print("record deleted succesfully")
except mysql.connector.Error as e:
    print("failed to fectable record{}".format(e))
finally:
    if con.is_connected():
        con.close()
        cur.close()
        print("mqsql connection is closed")

