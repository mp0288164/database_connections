import mysql.connector
try:
    conn=mysql.connector.connect(host='localhost',database='mymca',user='root',password='manisha')
    myd="""ALTER TABLE employee1 DROP company_name"""
    cur=conn.cursor()
    cur.execute(myd)
    print("sucessfully done drop coloum company_name in employee1 table ")

except mysql.connector.Error as e:
    print("faild to drop coloum in employee table{}".format(e))
finally:
    if conn.is_connected():
        cur.close()
        conn.close()
