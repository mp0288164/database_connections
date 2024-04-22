import pandas as pd
import mysql.connector
con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
if con.is_connected():
    rollno=int(input("enter the rollno:-"))
    df1=pd.read_sql("select * from student where rollno='%s'"%(rollno),con)
    print(df1)
else:
    print("mysql connection probleam")