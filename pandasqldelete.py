import pandas as pd
#import create_engine from sqlalchemy
from sqlalchemy import create_engine
import pymysql
eng=create_engine('mysql+pymysql://root:manisha@localhost/mymca')
con=eng.connect()
print("connection succesful")
"""if con.is_connected():
"""
df1=pd.read_sql("select * from student",con)
print(df1)

#record delete
delrollno=int(input("enter the rollno if you wand delete:-"))
delindex=df1[df1['rollno']==delrollno].index
df1.drop(delindex,axis=0,inplace=True)
df1.to_sql('student',con,if_exists='replace')
print("record deleted successfully")

