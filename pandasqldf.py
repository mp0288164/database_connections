import pandas as pd
from sqlalchemy import create_engine
import pymysql
eng=create_engine('mysql+pymysql://root:manisha@localhost/mymca')
con=eng.connect()
print("connection sucessful")
dict={'rollno':[600,700,800,900,1000],'name':['jiya','kiya','liya','viya','ranu'],'marks':[212,345,567,678,890]}
print(dict)
df1=pd.DataFrame(dict)
print(df1)
df1.to_sql('student',con,index=False,if_exists='append')
print("record inserted successfully")