import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor()
    #str=" select * f
    str=" select sname from student where sname like %s"
    #t1=('a%',)
    ch=input("enter the first latter of name:-")
    t2=(ch+'%',)
    cur.execute(str,t2)
    rec=cur.fetchall()
    print(rec)
    
except mysql.connector.Error as e:
	print("error:-{}".format(e))
finally:
	if con.is_connected:
		cur.close()
		con.close()
		print("connection is closed")
    