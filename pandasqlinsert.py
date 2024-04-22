import pandas as pd
from sqlalchemy import create_engine
import pymysql
eng=create_engine('mysql+pymysql://root:manisha@localhost/mymca')
con=eng.connect()
print("connection is successful")
df1=pd.read_sql("select * from student",con)
print(df1)
rollno=int(input("enter the rollno:-"))
name=input("enter the name:-")
marks=int(input("enter the marks:-"))
df1['rollno']=rollno
df1['name']=name
df1['marks']=marks 
df1.to_sql('student',con,if_exists='replace',index=False)
print(df1)
print("record updeted sucessfully")
