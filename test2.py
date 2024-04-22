import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor()
    str="select sum(marks) from student where age>=5"
    cur.execute(str)
    rec=cur.fetchall()
    print(rec)
    
except mysql.connector.Error as e:
	print("error:-{}".format(e))
finally:
	if con.is_connected:
		cur.close()
		con.close()
		print("connection is closed")
    