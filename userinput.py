import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor(prepared=True)
    str=""" INSERT INTO student(rollno,sname,sclass,marks,age) VALUES(%s,%s,%s,%s,%s)"""    
    ch="y"
    while ch=="y":
        roll_no=int(input("enter student rollno:-"))
        sname=input("enter student name:- ")
        sclass=int(input("enter the class:-"))
        marks=int(input("enter the marks:-"))
        age=int(input("enter the age:-"))
        t=(roll_no,sname,sclass,marks,age)
        cur.execute(str,t)
        con.commit()
        ch=input("add more records y/n:-")
except mysql.connector.Error as e:
    print("failed to inserted data  in student table{}".format(e))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("connection is closed")