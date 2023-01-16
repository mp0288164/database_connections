import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor(prepared=True)
    str="""INSERT INTO employee2(id,name,joining_date,salary)VALUES(%s,%s,%s,%s)"""
    t1=(1,"reena",2019-3-8,1900)
    t2=(2,"meena",2018-13-8,4900)
    cur.execute(str,t1)
    cur.execute(str,t2)
    con.commit()
    print("data insert sucessfully into employee table using the prepared statement")
except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("mysql connection is closed")

