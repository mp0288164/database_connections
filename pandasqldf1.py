import pandas as pd
from sqlalchemy import create_engine
import pymysql
eng=create_engine('mysql+pymysql://root:manisha@localhost/mymca') 
con=eng.connect()
rollno=[]
name=[]
marks=[]
no=int(input("enter the range of record do you want to insert:-"))
while no>0:
    r=int(input("enter the rollno:-"))
    rollno.append(r)
    n=input("enter the name:-")
    name.append(n)
    m=input("enter the marks:-")
    marks.append(m)
    no=no-1
dict={'rollno':rollno,'name':name,'marks':marks}
print(dict)
df1=pd.DataFrame(dict)
print(df1)
df1.to_sql('student',con,index=True,if_exists='append')
print("record inserted successfully")

   