import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    cur=con.cursor()
   
    #str="select * from bankaccount"
    #cur.execute(str)
    # widarw money
    debit_amount=int(input("enter the amunot do you want to debit:-"))
    waccno=int(input("please enter your account number:-"))
    str1="update bankaccount set balance=balance-%s where account_id=%s"
    t1=(debit_amount,waccno)
    print("hello")
	
    cur.execute(str1,t1)
    print("transaction successful")

    #con.commit()
    
    #deposit ammunt
    daccno=int(input("please enter the account number:-"))
    str2="update bankaccount set balance=balance+%s where account_id=%s"
    t2=[debit_amount,daccno,]
    cur.execute(str2,t2)
    con.commit()
    print("trancsation successful")

#except mysql.connector.Error as e:
    #print("failed transaction {}".format(e))
    #con.rollback()
except Exception as e:
	print(e)
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("connection is closed")
