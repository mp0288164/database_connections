import mysql.connector
import pandas  as pd
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor()
    str="select * from student"
    cur.execute(str)
    rec=cur.fetchall()
    print(rec)
    cloumns=cur.description
    #result=[{coloumns[index][0]:column for index,column in enumerate(value)} for value in cur.fetchall()]
    #print(result)
    df=pd.DataFrame(rec,columns=['Rollno','Name','Class','Marks','Age'])
    #str1="select sum(marks) from student"
    #cur.execute(str1)
    #sum=cur.fatchall()
    print(df)
    #print("sum of marks of all student:-",sum)
    
except mysql.connector.Error as e:
    print("Failed to fetchable recorde:{}".format(e))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("connection is closed")
