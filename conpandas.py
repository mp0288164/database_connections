import pandas as pd
import mysql.connector
con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
if con.is_connected():
    df1=pd.read_sql("select * from student",con)
    print(df1)
else:
    print("mysql connection probleam")
