import mysql.connector
import time

mydb = mysql.connector.connect(
        host = "34.85.64.241",
        user = "jts",
        passwd = "Jts5678?",
        database = "jtsboard_new"
        )
mycursor = mydb.cursor()


def insert_into_customers_table(c_name,c_kana,c_dob,c_tel):

    na = c_name.split(' ')
    if len(na) == 1:
        c_first_name = na[0] 
        c_last_name = "" 
    else:
        c_first_name = na[1] 
        c_last_name = na[0] 

    nna = c_kana.split(' ')
    if len(nna) == 1:
        c_kana_first_name = nna[0] 
        c_kana_last_name = "" 
    else:
        c_kana_first_name = nna[1] 
        c_kana_last_name = nna[0] 
    
    select_sql = """select * from customers where user_id = 102 and name = %s and tel = %s"""
    select_tuple = (c_name,c_tel)
    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()

    
    if len(myresult_list) == 0:
        insert_sql = """
            insert into customers (user_id,name,first_name,last_name,kana,kana_first_name,kana_last_name,dob,tel) 
            values(102,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        insert_tuple = (c_name,c_first_name,c_last_name,c_kana,c_kana_first_name,c_kana_last_name,c_dob,c_tel)
        mycursor.execute(insert_sql,insert_tuple)
        mydb.commit() 
        
        select_sql1 = """select * from customers where user_id = 102 and name = %s and tel = %s"""
        select_tuple1 = (c_name,c_tel)
        mycursor.execute(select_sql1,select_tuple1)
        myresult_list = mycursor.fetchall()
        
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
    else:
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
   
    return c_id


name="Kumarr3 Samanvayyy"
#name="咲依 糟谷"
nickname = "Ku Sa"
dob = "2019-01-01 00:00:00" 
tel = "221"
#tel = "09066423400"

id = insert_into_customers_table(name,nickname,dob,tel)
print(id)


"""
c_id 127
c_name 咲依 糟谷
c_kana_first_name サヨ
c_kana_last_name カスヤ
c_first_name 咲依
c_last_name
糟谷
c_kana
サヨ カスヤ
c_dob
1993-12-08
c_tel
09066423400
""" 
