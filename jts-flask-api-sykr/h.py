import mysql.connector
import random
from datetime import datetime

mydb = mysql.connector.connect(
        host = "34.85.64.241",
        user = "jts",
        passwd = "Jts5678?",
        database = "jtsboard_new"
        )

mycursor = mydb.cursor(buffered=True)


slot_list = ["00:00:00","00:30:00","01:00:00","01:30:00","02:00:00","02:30:00","03:00:00","03:30:00",
             "04:00:00","04:30:00","05:00:00","05:30:00","06:00:00","06:30:00","07:00:00","07:30:00",
             "08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00",
             "12:00:00","12:30:00","13:00:00","13:30:00","14:00:00","14:30:00","15:00:00","15:30:00",
             "16:00:00","16:30:00","17:00:00","17:30:00","18:00:00","18:30:00","19:00:00","19:30:00",
             "20:00:00","20:30:00","21:00:00","21:30:00","22:00:00","22:30:00","23:00:00","23:30:00"]


def get_employee_schedule_for_date(date_time_obj,employee_list):

    date_format = date_time_obj.strftime("%Y-%m-%d")
    employee_schedule_dict = {}

    for employee in employee_list:
        print("here")
        employee_schedule = [] 
        for i in range(48):
            employee_schedule.append(0)

        select_sql = """
            select service_id, employee_ids, start_date, start_time, end_time 
            from reservations where reservation_type='1' 
            and start_date = %s and employee_ids = %s
        """

        select_tuple = (date_format, employee)
        mycursor.execute(select_sql,select_tuple)

        appointments = mycursor.fetchall()

        for appointment in appointments:
            #print("--- appointment ---")
         
            service_id = appointment[0]
            employee_id = appointment[1]
            date = appointment[2]
            start_time = appointment[3]
            end_time = appointment[4]
            start_hour = start_time.seconds//3600
            start_minute = (start_time.seconds//60) % 60 
         
            start_slot_number = start_hour * 2
            if start_minute >= 30 and start_minute <= 59:
                start_slot_number += 1 
         
            end_hour = end_time.seconds//3600
            end_minute = (end_time.seconds//60) % 60 
         
            end_slot_number = end_hour * 2
         
            if end_minute == 0:
                end_slot_number -= 1 
            if end_minute > 30 and end_minute <= 59:
                end_slot_number += 1 
             
            for i in range(start_slot_number,end_slot_number+1):
                employee_schedule[i] = 1
 
        employee_schedule_dict[employee] = employee_schedule

    return employee_schedule_dict



def check_emp_avail_for_time(employee_schedule_dict,start_time,time_duration_in_hours):
    result_dict = {}
    num_of_slots_needed = time_duration_in_hours * 2

    start_time_split = start_time.split(":")
    start_hour = int(start_time_split[0])
    start_minute = int(start_time_split[1])

    print(start_hour)
    print(start_minute)

    start_slot_number = start_hour * 2
    if start_minute >= 30 and start_minute <= 59:
        start_slot_number += 1 
    next_slot_number = start_slot_number + num_of_slots_needed

    print(start_slot_number)
    print(next_slot_number)



    for employee in employee_schedule_dict:
        print("-------------------------")
        zero_count = 0
        for slot_i in range(start_slot_number,next_slot_number):
            if employee_schedule_dict[employee][slot_i] == 1:
                zero_count = 0
            else:
                zero_count += 1
            if zero_count == num_of_slots_needed:
                break

        avail_end_slot = slot_i
        avail_start_slot = avail_end_slot - num_of_slots_needed + 1

        print(avail_start_slot)
        print(avail_end_slot)


        free_slots = [avail_start_slot,]

        result_dict[employee] = free_slots 
     
    return result_dict











date_time_str = '09/09/18'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
employee_list = [56,57,59,67,111]

employee_schedule_dict1 = get_employee_schedule_for_date(date_time_obj,employee_list)
start_time1 = "10:00"
time_duration_in_hours1 = 3

x = check_emp_avail_for_time(employee_schedule_dict1,start_time1,time_duration_in_hours1)
print(x)


def generate_reservation_number():
    print("run")
    low =  100000000
    high =  999999999
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    al = random.choice(letters)
    num = str(random.randint(low,high))
    new_code = al + num
    sql = """select reservation_number from reservations"""
    mycursor.execute(sql)
    myresult_list = mycursor.fetchall()
    found = 0
    for code_tuple in myresult_list:
        exist_code_ba = code_tuple[0]
        exist_code = exist_code_ba.decode() ; exist_code
        if new_code == exist_code:
            found = 1
            break
    if found == 0:
        return new_code
    elif found == 1:
        generate_reservation_number()

#x = generate_reservation_number()
#print(x)





def get_sub_services(service_id):
    sql = """select id,name,duration,price from sub_services where user_id = 102 and status = 1 and service_id = %s"""
    select_tuple = (service_id,)
        
    mycursor.execute(sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    
    ss_dict = dict()
    menu_int = 1

    for serv_tuple in myresult_list:
        #print("_______")

        ss_id = serv_tuple[0]
        
        serv_tuple_second = serv_tuple[1]
        ss_name = serv_tuple_second.decode() ; ss_name 
        
        serv_tuple_third = serv_tuple[2]
        ss_duration = serv_tuple_third.decode() ; ss_duration 
        
        serv_tuple_fourth = serv_tuple[3]
        ss_price = serv_tuple_fourth.decode() ; ss_price

        ss_dict[menu_int] = {"id": ss_id, "item": ss_name, "duration": ss_duration, "price": ss_price}
        
        menu_int += 1

    return ss_dict


        #print("id",ss_id)
        #print("name",ss_name)
        #print("duration",ss_duration)
        #print("price",ss_price) 

def find_employees_for_service(service_id):

    sql = """select service_id,id from employees where user_id = 102 and is_technician = 1 order by service_id"""
    mycursor.execute(sql)
    myresult_list = mycursor.fetchall()

    service_dict = dict()

    for serv_tuple in myresult_list:
        if serv_tuple[0] in service_dict:
            service_dict[serv_tuple[0]].append(serv_tuple[1])
        else:
            service_dict[serv_tuple[0]] = [serv_tuple[1]]


    return service_dict[service_id]



#s = get_sub_services(1)
#print(s)



