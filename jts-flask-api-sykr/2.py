import mysql.connector

mydb = mysql.connector.connect(
        host = "34.85.64.241",
        user = "jts",
        passwd = "Jts5678?",
        database = "jtsboard_new"
        )
mycursor = mydb.cursor()


def insert_into_reservations_table(u_id,c_id,s_id,ss_id,e_id,s_date,e_date,s_time,e_time,total):

    ex_s_date = s_date + " 00:00:00"
    ex_e_date = e_date + " 00:00:00" 


    insert_sql = """
        insert into reservations
        (id,user_id,customer_id,service_id,sub_service_id,employee_ids,
        start_date,end_date,extra_start_date,extra_end_date,start_time,end_time,
        reservation_type,reservation_total,used_points,payment_total,status) 
        values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'1',%s,'0',%s,1)
    """
   
    insert_tuple = (u_id,c_id,s_id,ss_id,e_id,s_date,e_date,ex_s_date,ex_e_date,s_time,e_time,total,total)
    mycursor.execute(insert_sql,insert_tuple)
    mydb.commit()
    #return "nothing" 

i_u_id=102
i_c_id=501
i_s_id=1
i_ss_id=11
i_e_id="49"
i_s_date="2019-09-09"
i_e_date="2019-09-09"
i_s_time="14:00:00"
i_e_time="15:00:00"
i_total="6,800 円"

id = insert_into_reservations_table(i_u_id,i_c_id,i_s_id,i_ss_id,i_e_id,i_s_date,i_e_date,i_s_time,i_e_time,i_total)
print(id)

