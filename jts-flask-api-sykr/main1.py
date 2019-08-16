# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:45:55 2019

@author: hp
"""

from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from flask import request
from datetime import datetime

from flask_cors import CORS, cross_origin
from wtforms import TextField,TextAreaField, SubmitField
from wtforms.validators import Required
 
import sys
import os
import datetime
import calendar

import pickle

import json


########################################################################
######### CHAT BOT VARIABLES
########################################################################

import mysql.connector
import datetime
import time
from dateutil import relativedelta
from flask import Flask, jsonify, request
import os
import traceback
import json
import random

now = datetime.datetime.now()
now1= now + datetime.timedelta(days=1)
now2= now + datetime.timedelta(days=2)
now3= now + datetime.timedelta(days=3)
now4= now + datetime.timedelta(days=4)
now5= now + datetime.timedelta(days=5)
now6= now + datetime.timedelta(days=6)

# Define the messages

all_okay_message = """
    All Okay.
    
    """

welcome_ask_name_message = """
    こんにちは。アプリ登録ありがとうございます。
    私の名前はミライです。
    私は、あなた専属の美容コンシェルジュです。
    サロンの予約受付は私が行います。
    さらに、
    サロンのこと、
    美容のこと、
    わからないことがあれば何でも解決策を考えます。
    知りたい情報はいち早くお伝えいたします。
    あなたの人生が楽しく、そして快適に過ごせるように・・・
    全力でお手伝いいたします。
    どうぞよろしくお願いいたします。
    
    あなたのお名前は？
    
    """


is_nickname_message = """
    とっても可愛いお名前ですね。
    ニックネームはありますか？
    
    """


is_confirm_message = """
    確認しますか？
    
    """

wrong_is_nickname_message = """
    ニックネームがあるかどうかについて有効な応答を入力してください。
    はいの場合は1、いいえの場合は2を押します。
    
    """

wrong_is_reservation_now_message = """
    今すぐ予約するかどうかの有効な回答を入力してください。
    「はい」の場合は1、「いいえ」の場合は2を押します。
    """

wrong_is_time_for_more_message = """
    他に質問があるかどうかについて、有効な回答を入力してください。
    はいの場合は1、いいえの場合は2を押します。 
    """

wrong_is_confirm_message = """
    Please type a valid response which I can understand.
    Press 1 for Yes or 2 for No.
    
    """
wrong_cust_type_of_salon_message = """
    Please type a valid type of salon from the options provided.
    
    """
wrong_cust_service_message = """
    Please type a valid service from the options provided.
    
    """
wrong_cust_avail_options_message = """
    Please type a valid staff/time from the options provided.
    
    """
wrong_cust_sub_service_message = """
    Please type a valid menu item from the options provided.
    
    """



ask_nickname_message = """
    ニックネームは何ですか？
    
    What is your nickname?
    
    """

ask_birthday_message = """
    いいですね。ありがとうございました{0}。
    今後も仲良くしてください。
    
    お誕生日を教えていただけますか {1}？
   
    例：2019年6月21日に21-06-2019と入力します。
     
    Great, thank you {2}, we are going to be best friends.
    
    May I know your birthday {3}?

    Example: enter 21-06-2019 for 21 June 2019.
    
    """
ask_birthday_without_nickname_message = """
    お誕生日を教えていただけますか？
   
    例：2019年6月21日に21-06-2019と入力します。
     
    May I know your birthday?

    Example: enter 21-06-2019 for 21 June 2019.
    
    """



is_time_for_more_message = """
    そうなんですね。
    もう少し質問に答えていただける時間はありますか？
    
    oh, cool,
    do you have time for more questions or we can talk later?
    
    """

ask_phone_message = """
    ありがとうございます。
    電話番号を教えてください。
    
    Thank you very much,
    What is your phone number?
    
    """

ask_color_message = """
    ありがとうございます。
    {0}、何色がお好きですか？
    
    Oh, I’m so happy we can talk now,
    {1}, what is your favorite color?
    
    """
ask_color_without_nickname_message = """
    ありがとうございます。
    何色がお好きですか？
    
    Oh, I’m so happy we can talk now,
    what is your favorite color?
    
    """
def color_menu_int_to_idea(argument):
    argument = int(argument)
    switcher = {
        1:	"warmth and love",
        2:	"care and nurture",
        3:  "cheerfulness and creativity",
        4:  "comfort and liveliness",
        5:  "durability and optimism",
        6:	"professionalism and loyalty",
        7:  "royalty and nobility",
        8:  "traditionalism and intelligence", 
        9:  "confidence and reliabilty",
        10: "elegance and sophistication", 
        11: "peace and simplicity"
    }
    return switcher.get(argument, "nothing")


def color_menu_int_to_name(argument):
    print("Inside Switcher")
    print("Argument:" + str(argument) + "Arg")
    print(type(argument))
    try:
        argument = int(argument)
    except:
        return "nothing"
     
    switcher = {
        1:	"red",
        2:	"pink",
        3: "orange",
        4: "yellow",
        5: "green",
        6:	"blue",
        7:  "purple",
        8:  "gray", 
        9: "brown",
        10: "black", 
        11: "white"
    }

    #x = switcher[argument]
    #print(x)
    return switcher.get(argument, "nothing")

old_ask_type_of_salon_message = """
    いい色ですよね。この色は・・・
    
    どんな美容サロンが好きですか？
    
    1) 早く仕上げてくれる。
    2) 安い。
    3) 静かなサロン。
    4) 接客がとてもいいサロン。
    5) 高級感のあるサロン。
    6) スタッフの質が高いサロン。
    7) 清潔感のあるサロン。
    8) 落ち着いたサロン。
    
    
    Oh nice color, this color represent ………
    
    What type of beauty salons do you like?
    
    1) Fast salon,
    2) Cheap price,
    3) Quite salon,
    4) Salon where I can have a good conversation and get good treatment,
    5) Expensive salon,
    6) High quality salon staff
    7) Salon with cleanliness
    8) Calm Salon
    
    """

ask_type_of_salon_message = """
    いい色ですよね。この色は {0}
    
    どんな美容サロンが好きですか？
    
    Oh nice color, this color represent {1}
    
    What type of beauty salons do you like?
    """

is_reservation_now_message = """
    わかりました。
    お客様の期待に答えられるように、努めてまいります。
    
    次回予約をお取りしましょうか？
    
    I understand, I will always try to find you best options and best services for you,
    
    Would you like to make a reservation at your salon for next time? Or later?
    
    
    """

ask_date_message = """
    かしこまりました。
    ご予約のお日にちはいつがよろしいですか？
    例：2019年6月21日に21-06-2019と入力します。
    
        
    Okay, when you like to visit?
    Example: enter 21-06-2019 for 21 June 2019.
    
    """

ask_service_message = " メニューはお決まりですか？/ What you like to do? "
#    メニューはお決まりですか？/ What you like to do?
#    What you like to do?
#    
#    """

empty_name_message = """
    I am pretty sure you have a wonderful name.
    
    Please tell me. I won't tell anyone.
    
    """

empty_nickname_message = """
    Hmm.. I guess you forgot to type your nickname.
    
    """


good_name_message = """
    That's a nice name, {}.
    
    Please let me know your phone number as well.
    
    """

good_phone_message = """
    Thanks for the number.
    
    Currently, we have 3 services:
    
    1) Nails
    2) Beauty treatment
    3) Eye lashes
    
    What would you like?
    
    """

empty_phone_message = """
    I need your phone number to serve you better.
    Don't worry I won't call you in odd hours.
    
    """
wrong_color_message = """
    Please choose a correct option for color between 1 to 11.
    
    """



wrong_service_message = """
    Please choose a correct option from 1 to 3.
    
    """

good_service_message = """
    Sounds Good.
    
    What date would you like to visit our salon?
    
    Example: enter 21-06-2019 for 21 June 2019.
    
    """

wrong_date_message = """
    Please enter the correct date in a format I understand.
    
    Example: enter 21-06-2019 for 21 June 2019
    
    """

good_date_message = """
    Alright!
    
    What time would be convenient for you?
    
    Example: enter 13:00 for 1pm
    
    """
good_time_message = """
    Checking availablity of our staff.
    
    Please wait.
    
    """


get_time_message = """
    Alright!
    
    What time would be convenient for you?
    
    Example: enter 13:00 for 1pm
    """

wrong_time_message = """
    Please enter the correct time in a format I understand.
    
    Example: enter 13:00 for 1pm
    """

select_date_message = """
    Okay, Please tell me which date.
    1) %s
    2) %s
    3) %s
    4) %s
    5) %s
    6) %s
    7) %s
    """  % (now.strftime("%Y-%m-%d"),now1.strftime("%Y-%m-%d"),now2.strftime("%Y-%m-%d"),now3.strftime("%Y-%m-%d"),now4.strftime("%Y-%m-%d"),now5.strftime("%Y-%m-%d"),now6.strftime("%Y-%m-%d"))

sorry_recommend_message = """
    Sorry, This day is not available.
    I recommend that you schedule an appointment for %s
    """

available_recommend_message = """
    This day is available !!!
    However, I recommend that you schedule an appointment for %s
    """
confirm_date_message = """
    Please confirm your booking date.
    """
exit_message = """
    Your appointment is booked.
    I hope to see you soon.
    """

booking_message = """
    Booking your appointment.
    Please Wait.
    """
confirm_sorry_message = """
    Sorry, This day is not available.
    Please choose another date.
    """



"""
local_connection = mysql.connector.connect(
                                           host="localhost",
                                           user="root",
                                           passwd="12345678",
                                           database="test"
                                           )

local_cursor = local_connection.cursor()
"""


mydb = mysql.connector.connect(
                               host="34.85.64.241",
                               user="jts",
                               passwd="Jts5678?",
                               database="jtsboard_new"
                               )
mycursor = mydb.cursor()

slot_list = ["00:00:00","00:30:00","01:00:00","01:30:00","02:00:00","02:30:00","03:00:00","03:30:00",
             "04:00:00","04:30:00","05:00:00","05:30:00","06:00:00","06:30:00","07:00:00","07:30:00",
             "08:00:00","08:30:00","09:00:00","09:30:00","10:00:00","10:30:00","11:00:00","11:30:00",
             "12:00:00","12:30:00","13:00:00","13:30:00","14:00:00","14:30:00","15:00:00","15:30:00",
             "16:00:00","16:30:00","17:00:00","17:30:00","18:00:00","18:30:00","19:00:00","19:30:00",
             "20:00:00","20:30:00","21:00:00","21:30:00","22:00:00","22:30:00","23:00:00","23:30:00"]



def insert_into_chats_db(user_id,ip,name,is_nickname,nickname,birthday,is_time_for_more,phone,color,type_of_salon,is_reservation_now,res_date,res_time,service_id,emp_id,is_confirm,last_state):

    sql = "insert into chats values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    insert_tuple = (user_id,ip,name,is_nickname,nickname,birthday,is_time_for_more,phone,color,type_of_salon,is_reservation_now,res_date,res_time,service_id,emp_id,is_confirm,last_state)
    
    mycursor.execute(sql,insert_tuple)
    
    mydb.commit()



def insert_into_session_db(ip,STATE,return_list_of_dicts,return_dict,cust_responses):

    print("\n\nInside insert session\n\n")
    print("HHHHHHHHHHH" + return_list_of_dicts + "IIIIIIIIIIII")
    #return "nothing"

    #sql = "insert into session(ip,STATE,return_list_of_dicts,return_dict,cust_responses) values(%s,%s,%s,%s,%s)"
    sql = "insert into sessions(ip,STATE,return_list_of_dicts,return_dict,cust_responses) values(%s,%s,%s,%s,%s)"
    
    insert_tuple = (ip,STATE,return_list_of_dicts,return_dict,cust_responses)
    
    mycursor.execute(sql,insert_tuple)
    
    mydb.commit()


def update_session_db(ip,STATE,return_list_of_dicts,return_dict,cust_responses):
    
    print("\n\n\nLLLLLLLLLLLLLLLLLLLLL\n\n\n")
    print("IP:",ip) 
    #sql = "update session set STATE = %s, return_list_of_dicts = %s, return_dict = %s,cust_responses= %s where ip = %s"
    sql = "update sessions set STATE = %s, return_list_of_dicts = %s, return_dict = %s,cust_responses= %s where ip = %s"
    insert_tuple = (STATE,return_list_of_dicts,return_dict,cust_responses,ip)
    mycursor.execute(sql,insert_tuple)
    mydb.commit()


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



def insert_into_reservations_table(u_id,c_id,s_id,ss_id,e_id,s_date,e_date,s_time,e_time,total):

    ex_s_date = s_date + " 00:00:00"
    ex_e_date = e_date + " 00:00:00" 
    r_num = generate_reservation_number() 
    now_obj = datetime.datetime.now()
    now_str = str(now_obj)
    print("generated code successfully")

    insert_sql = """
        insert into reservations
        (id,user_id,customer_id,service_id,
        sub_service_id,employee_ids,reservation_number,
        start_date,end_date,extra_start_date,
        extra_end_date,start_time,end_time,
        reservation_type,reservation_total,
        used_points,payment_total,status,created,modified)
        values(default,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'1',%s,'0',%s,1,%s,%s)
    """
   
    insert_tuple = (
        u_id,c_id,s_id,ss_id,e_id,r_num,s_date,e_date,
        ex_s_date,ex_e_date,s_time,e_time,total,total,
        now_str,now_str
    )

    mycursor.execute(insert_sql,insert_tuple)
    mydb.commit()



def insert_into_customers_table(c_name,c_kana,c_dob,c_tel,user_id):

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
    
    select_sql = """select * from customers where user_id = %s and name = %s and tel = %s"""
    select_tuple = (user_id,c_name,c_tel)

    mycursor.execute(select_sql,select_tuple)
    myresult_list = mycursor.fetchall()

    
    if len(myresult_list) == 0:
        now_obj = datetime.datetime.now()
        now_str = str(now_obj)
        insert_sql = """ 
            insert into customers (user_id,name,first_name,last_name,kana,
            kana_first_name,kana_last_name,dob,tel,created,modified) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        insert_tuple = (
            user_id,c_name,c_first_name,c_last_name,
            c_kana,c_kana_first_name,c_kana_last_name,
            c_dob,c_tel,now_str,now_str
        )

        mycursor.execute(insert_sql,insert_tuple)
        mydb.commit() 

        select_sql1 = """select * from customers where user_id = %s and name = %s and tel = %s"""
        select_tuple1 = (user_id,c_name,c_tel)
        mycursor.execute(select_sql1,select_tuple1)
        myresult_list = mycursor.fetchall()
    
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
    else:
        tuple0 = myresult_list[0]
        c_id = tuple0[0]
   
    return c_id


def find_employee_name(user_id):
    select_sql = """select id,name from employees where user_id = %s and is_technician = 1 order by service_id """
    select_tuple = (user_id,) 
    mycursor.execute(select_sql,select_tuple)

    myresult_list = mycursor.fetchall()
    emp_name_dict = dict()

    for emp_tuple in myresult_list:
        emp_name_dict[emp_tuple[0]] = [emp_tuple[1]]

    return emp_name_dict


def get_services(user_id):

    print("user_id")
    print(user_id)

    select_sql = """
        select id, name from services where id in 
        (select distinct service_id from employees 
        where user_id = %s and is_technician = 1 and service_id in 
        (select distinct service_id from sub_services where user_id = %s));
    """

    select_tuple = (user_id,user_id)
    
    mycursor.execute(select_sql,select_tuple)
    
    myresult_list  = mycursor.fetchall()
    
    s_dict = dict()
    menu_int = 1 

    for serv_tuple in myresult_list:
        #print("_______")

        s_id = serv_tuple[0]
    
        serv_tuple_second = serv_tuple[1]
        s_name = serv_tuple_second.decode() ; s_name 

        s_dict[str(menu_int)] = {"id": s_id, "name": s_name}
    
        menu_int += 1

    return s_dict



def get_sub_services(service_id,user_id):

    print("inside get sub serices")
    print("service_id","user_id")
    print(service_id,user_id)
    sql = """select id,name,duration,price from sub_services where user_id = %s and status = 1 and service_id = %s"""
    select_tuple = (user_id,service_id)
    
    mycursor.execute(sql,select_tuple)
    myresult_list  = mycursor.fetchall()
    print("myresult_list") 
    print(myresult_list) 
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

        ss_dict[str(menu_int)] = {"id": ss_id, "item": ss_name, "duration": ss_duration, "price": ss_price}
    
        menu_int += 1
    print("ss_dict")
    print(ss_dict)

    return ss_dict

def find_employees_for_service(service_id,user_id):


    print("inside find employees for service")
    print("service_id,user_id")
    print(service_id,user_id)
    
    select_sql = """select service_id,id from employees where user_id = %s and is_technician = 1 order by service_id"""
    select_tuple = (user_id,)
    mycursor.execute(select_sql,select_tuple)

    myresult_list = mycursor.fetchall()

    print("myresult_list")
    print(myresult_list)
        
    service_dict = dict()

    for serv_tuple in myresult_list:
        if serv_tuple[0] in service_dict:
            service_dict[serv_tuple[0]].append(serv_tuple[1])
        else:
            service_dict[serv_tuple[0]] = [serv_tuple[1]]

    print("service_dict[service_id]")
    print(service_dict[service_id])

    return service_dict[service_id]

#def check_availability(service_int, date_time_obj,employee_list,time_duration):
#    return result_list


def check_new_availability(date_time_obj,employee_list,time_duration,user_id):
    print("Check New Availability")
    print("date_time_obj,employee_list,time_duration,user_id")
    print(date_time_obj,employee_list,time_duration,user_id)
    #return 0

    result_dict = {}
    date_format = date_time_obj.strftime("%Y-%m-%d")
    time_format = date_time_obj.strftime("%H:%M:%S")
    
    for employee in employee_list:
        print("\n\n\nEmployee\n\n\n")
        employee_schedule = []
        for i in range(48):
            employee_schedule.append(0)

        select_sql = """select service_id, employee_ids, start_date, start_time, end_time from reservations where user_id = %s and reservation_type='1' and start_date = %s and employee_ids = %s"""

        select_tuple = (user_id, date_format, employee)
        mycursor.execute(select_sql,select_tuple)

        appointments = mycursor.fetchall()
        for appointment in appointments:
            print("--- appointment ---")
            #print(appointment) 
            
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

        print("employee_schedule")
        print(employee_schedule)
    #return 0

     
        num_of_slots_needed = time_duration * 2

        free_slots = []

        slot_i = 20 # Starting at 10:00 AM

        for i in range(3):
            #print("Iteration " + str(i) + " Started")
            zero_count = 0
            
            if i != 0 :     ## Increase slot number
                slot_i += 1 ## from previous iteration
            
            while slot_i <= 44: # Ending search at 10:00 PM
                #print("Inside While Loop")
                #print("slot = " + str(slot_i))
                if employee_schedule[slot_i] == 1:
                    zero_count = 0
                else:
                    zero_count += 1
                
                if zero_count == num_of_slots_needed:
                    break
                slot_i += 1

            avail_end_slot = slot_i
            avail_start_slot = avail_end_slot - num_of_slots_needed + 1
        
            free_slots.append(avail_start_slot)
            result_dict[employee] = free_slots
     
    print("result_dict")
    print(result_dict)
    return result_dict


def convert_avail_dict_to_display_options(avail_dict,emp_name_dict):
    print("Convert Avail Dict TO Display Options") 
    print("avail_dict,emp_name_dict")
    print(avail_dict,emp_name_dict)
    #return 0,0,0 
    
    avail_msg = "かしこまりました。次のお日にちで空きがあります。\n"
    avail_msg = avail_msg + "Okay, we have availability at the following times:\n"
    option_list = []
    option_new_list = []
    display_options = []

    emp_serial = 1
    
    for emp_id in avail_dict:
        list_of_avail_slots = avail_dict[emp_id]
        for slot in list_of_avail_slots:
            time_start = slot_list[slot]
            
            emp_bytearray_list = emp_name_dict[emp_id]
            emp_bytearray_firstelement = emp_bytearray_list[0]
            emp_name = emp_bytearray_firstelement.decode() ; emp_name
            option_str = str(emp_serial) + ") " + emp_name + " is available at " + str(time_start)
            option_list.append(option_str)

            key = str(emp_serial)
            value = emp_name + " is available at " + str(time_start)

            my_dict = {
                "key": key,
                "value": value
            }
            option_new_list.append(my_dict)
            option = [emp_serial,emp_id,slot]
            display_options.append(option)
            emp_serial += 1

    none_option_str = str(emp_serial) + ") " + "None of the above times suit me."
    option_list.append(none_option_str)

    none_key = str(emp_serial)
    none_value = "None of the above times suit me."
    none_dict = {
    "key": none_key,
    "value": none_value
    }
    option_new_list.append(none_dict)

    none_option = [emp_serial,"none","none"]
    display_options.append(none_option)

    print("display_options,option_new_list")
    print(display_options,option_new_list)

    return avail_msg,display_options,option_new_list




def type_of_salon_menu_int_to_name(argument):
    switcher = {
    1: "早く仕上げてくれる",
    2: "安い",
    3: "静かなサロン",
    4: "接客がとてもいいサロン",
    5: "高級感のあるサロン",
    6: "スタッフの質が高いサロン",
    7: "清潔感のあるサロン",
    8: "落ち着いたサロン"

    }

    return switcher.get(argument, "nothing")

"""
def service_menu_int_to_id(argument):
    switcher = {
    1: 1,
    2: 3,
    3: 2
    }

    return switcher.get(argument, "nothing")
"""


def service_menu_int_to_id(argument):
    switcher = {
    1: 1,
    2: 2
    }

    return switcher.get(argument, "nothing")


def service_numbers_to_strings(argument):
    switcher = {
    1: "nails",
    2: "beauty_treatment",
    3: "eye_lashes",
    4: "body",
    5: "hair_removal",
    6: "facial"
    }
    return switcher.get(argument, "nothing")


def welcome_the_user():
    return welcome_message


def welcome_ask_name():
    return welcome_ask_name_message


def is_nickname_fun():
    is_nickname_options = [ 
    {"key":"1", "value":"はい / Yes"}, 
    {"key":"2","value": "いいえ / No"} 
    ]
    return is_nickname_message,is_nickname_options

def ask_nickname():
    return ask_nickname_message

def ask_birthday(cust_responses):
    if cust_responses["is_nickname"] == "yes":
        nick = cust_responses["nickname"]
        return ask_birthday_message.format(nick,nick,nick,nick)
    else:
        return ask_birthday_without_nickname_message

def is_time_for_more_fun():
#is_time_for_more_options = ["1) はい、今から大丈夫です。/ I can chat now", "2) 今は難しいです。/ let’s talk later"]

    is_time_for_more_options = [ 
    {"key":"1", "value": "はい、今から大丈夫です。/ I can chat now"}, 
    {"key":"2", "value": "今は難しいです。/ let’s talk later"} 
    ]

    """ 
    is_time_for_more_options = {
    "1" :"はい、今から大丈夫です。/ I can chat now", 
    "2": "今は難しいです。/ let’s talk later"
    }
    """

    return is_time_for_more_message,is_time_for_more_options

def ask_phone():
    return ask_phone_message

def ask_color(cust_responses):

#color_options = ["1) red","2) pink","3) orange","4) yellow","5) green","6) blue","7) purple","8) gray","9) brown","10) black","11) white"]


#color_options = {"1": "red","2":"pink","3": "orange","4": "yellow","5": "green","6": "blue","7": "purple","8":"gray","9": "brown","10": "black","11": "white"}

    color_options = [  
    {"key":"1", "value": "red"}, 
    {"key":"2", "value": "pink"}, 
    {"key":"3", "value": "orange"},
    {"key":"4", "value": "yellow"},
    {"key":"5", "value": "green"},
    {"key":"6", "value": "blue"},
    {"key":"7", "value": "purple"},
    {"key":"8", "value": "gray"},
    {"key":"9", "value": "brown"},
    {"key":"10", "value": "black"},
    {"key":"11", "value": "white"}
    ]     


    if cust_responses["is_nickname"] == "yes":
        nick = cust_responses["nickname"]
        return ask_color_message.format(nick,nick),color_options
    else:
        return ask_color_without_nickname_message,color_options


def ask_type_of_salon(color_idea):
#ask_type_of_salon_options = ["1) 早く仕上げてくれる。/ Fast salon","2) 安い。/ Cheap price",
#                             "3) 静かなサロン。/ Quite salon","4) 接客がとてもいいサロン。/ Salon where I can have a good conversation and get good treatment",
#                             "5) 高級感のあるサロン。/ Expensive salon","6) スタッフの質が高いサロン。/ High quality salon staff",
#                             "7) 清潔感のあるサロン。/ Salon with cleanliness", "8) 落ち着いたサロン。/ Calm salon"]
    """ 
    ask_type_of_salon_options = {"1": "早く仕上げてくれる。/ Fast salon",
                             "2": "安い。/ Cheap price",
                             "3": "静かなサロン。/ Quite salon",
                             "4": "接客がとてもいいサロン。/ Salon where I can have a good conversation and get good treatment",
                             "5": "高級感のあるサロン。/ Expensive salon",
                             "6": "スタッフの質が高いサロン。/ High quality salon staff",
                             "7": "清潔感のあるサロン。/ Salon with cleanliness", 
                             "8": "落ち着いたサロン。/ Calm salon"}
    """
    ask_type_of_salon_options = [
    {"key":"1", "value": "早く仕上げてくれる。/ Fast salon"},
    {"key":"2", "value": "安い。/ Cheap price"},
    {"key":"3", "value": "静かなサロン。/ Quite salon"},
    {"key":"4", "value": "接客がとてもいいサロン。/ Salon where I can have a good conversation and get good treatment"},
    {"key":"5", "value": "高級感のあるサロン。/ Expensive salon"},
    {"key":"6", "value": "スタッフの質が高いサロン。/ High quality salon staff"},
    {"key":"7", "value": "清潔感のあるサロン。/ Salon with cleanliness"},
    {"key":"8", "value": "落ち着いたサロン。/ Calm salon"}
    ]   



    #color_idea = session['color_idea']
    return ask_type_of_salon_message.format(color_idea,color_idea), ask_type_of_salon_options

def is_reservation_now_fun():
#is_reservation_now_options = ["1) 予約を取る。/ Make a reservation","2) 後で予約を取る。/ Later"]
#is_reservation_now_options = {"1": "予約を取る。/ Make a reservation","2": "後で予約を取る。/ Later"}
    is_reservation_now_options = [
    {"key":"1", "value": "予約を取る。/ Make a reservation"},
    {"key":"2", "value": "後で予約を取る。/ Later"}
    ]   

    return is_reservation_now_message,is_reservation_now_options

def ask_date():
    return ask_date_message



def ask_service_fun(user_id):
    service_dict = get_services(user_id) 
    ask_service_options = []
    
    for service in service_dict:
        value = str(service_dict[service]["name"])
        option = {"key": service, "value": value} 
        ask_service_options.append(option)
    return ask_service_message, ask_service_options,service_dict


def ask_sub_service_fun(cust_responses):
    print("inside ask sub service function")

    ask_sub_service_message = "Please select an item from menu."
    sub_service_dict = cust_responses["sub_service_dict"] 
   
    ask_sub_service_options = []
    for sub_service in sub_service_dict:
        value = str(sub_service_dict[sub_service]["item"]) + " : " + str(sub_service_dict[sub_service]["price"])
        #option = {"key": sub_service, "value": sub_service_dict[sub_service]} 
        option = {"key": sub_service, "value": value} 
        ask_sub_service_options.append(option)
     
    return ask_sub_service_message,ask_sub_service_options



def show_avail_options():
    return session['cust_avail_msg']

def is_confirm():
#is_confirm_options = ["1) はい / Yes", "2) いいえ / No"]
#is_confirm_options = {"1": "はい / Yes", "2": "いいえ / No"}

    is_confirm_options = [
    {"key":"1", "value": "はい / Yes"},
    {"key":"2", "value": "いいえ / No"},
    ]

    return is_confirm_message,is_confirm_options


def ask_name():
    return get_name_message

def check_name(name):
    name_status = 0
    if not name:
        name_status = 0
        return name_status, empty_name_message
    else:
        name_status = 1
        return name_status, good_name_message


def check_is_nickname(is_nickname_menu_int):

    is_nickname_status = 0

    try:
        is_nickname_menu_int = int(is_nickname_menu_int)
    except:
        is_nickname_status = 0
        is_nickname_response = None
        out_msg = wrong_is_nickname_message
        return is_nickname_status, is_nickname_response, out_msg


    if is_nickname_menu_int != 1 and is_nickname_menu_int != 2:
        is_nickname_status = 0
        is_nickname_response = None
        out_msg = wrong_is_nickname_message

    if is_nickname_menu_int == 1:
        is_nickname_status = 1
        is_nickname_response = "yes"
        out_msg = all_okay_message

    if is_nickname_menu_int == 2:
        is_nickname_status = 1
        is_nickname_response = "no"
        out_msg = all_okay_message

    return is_nickname_status, is_nickname_response, out_msg

def check_is_confirm(is_confirm_menu_int):

    is_confirm_status = 0

    try:
        is_confirm_menu_int = int(is_confirm_menu_int)
    except:
        is_confirm_status = 0
        is_confirm_response = None
        out_msg = wrong_is_confirm_message
        return is_confirm_status, is_confirm_response, out_msg


    if is_confirm_menu_int != 1 and is_confirm_menu_int != 2:
        is_confirm_status = 0
        is_confirm_response = None
        out_msg = wrong_is_confirm_message

    if is_confirm_menu_int == 1:
        is_confirm_status = 1
        is_confirm_response = "yes"
        out_msg = all_okay_message

    if is_confirm_menu_int == 2:
        is_confirm_status = 1
        is_confirm_response = "no"
        out_msg = all_okay_message

    return is_confirm_status, is_confirm_response, out_msg



def check_is_reservation_now(is_reservation_now_menu_int):

    is_reservation_now_status = 0

    try:
        is_reservation_now_menu_int = int(is_reservation_now_menu_int)
    except:
        is_reservation_now_status = 0
        is_reservation_now_response = None
        out_msg = wrong_is_reservation_now_message
        return is_reservation_now_status, is_reservation_now_response, out_msg


    if is_reservation_now_menu_int != 1 and is_reservation_now_menu_int != 2:
        is_reservation_now_status = 0
        is_reservation_now_response = None
        out_msg = wrong_is_reservation_now_message

    if is_reservation_now_menu_int == 1:
        is_reservation_now_status = 1
        is_reservation_now_response = "yes"
        out_msg = all_okay_message

    if is_reservation_now_menu_int == 2:
        is_reservation_now_status = 1
        is_reservation_now_response = "no"
        out_msg = all_okay_message

    return is_reservation_now_status, is_reservation_now_response, out_msg


def check_nickname(nickname):
    nickname_status = 0
    if not nickname:
        nickname_status = 0
        return nickname_status, empty_nickname_message
    else:
        nickname_status = 1
        return nickname_status, all_okay_message


def check_is_time_for_more(is_time_for_more_menu_int):

    is_time_for_more_status = 0

    try:
        is_time_for_more_menu_int = int(is_time_for_more_menu_int)
    except:
        is_time_for_more_status = 0
        is_time_for_more_response = None
        out_msg = wrong_is_time_for_more_message
        return is_time_for_more_status, is_time_for_more_response, out_msg


    if is_time_for_more_menu_int != 1 and is_time_for_more_menu_int != 2:
        is_time_for_more_status = 0
        is_time_for_more_response = None
        out_msg = wrong_is_time_for_more_message

    if is_time_for_more_menu_int == 1:
        is_time_for_more_status = 1
        is_time_for_more_response = "yes"
        out_msg = all_okay_message

    if is_time_for_more_menu_int == 2:
        is_time_for_more_status = 1
        is_time_for_more_response = "no"
        out_msg = all_okay_message

    return is_time_for_more_status, is_time_for_more_response, out_msg


def check_cust_type_of_salon(cust_type_of_salon_menu_int):

    cust_type_of_salon_status = 0

    try:
        cust_type_of_salon_menu_int = int(cust_type_of_salon_menu_int)
    except:
        cust_type_of_salon_status = 0
        cust_type_of_salon_response = None
        out_msg = wrong_cust_type_of_salon_message
        return cust_type_of_salon_status, cust_type_of_salon_response, out_msg

    salon_type_name = type_of_salon_menu_int_to_name(cust_type_of_salon_menu_int)


    if salon_type_name == "nothing":
        cust_type_of_salon_status = 0
        cust_type_of_salon_response = None
        out_msg = wrong_cust_type_of_salon_message

    else:
        cust_type_of_salon_status = 1
        cust_type_of_salon_response = salon_type_name
        out_msg = all_okay_message

    return cust_type_of_salon_status, cust_type_of_salon_response, out_msg

def check_service(cust_service_menu_int,cust_responses):
    
    cust_service_status = 0
    try:
        cust_service_menu_int = int(cust_service_menu_int)
    except:
        
        cust_service_status = 0
        cust_service_id = None
        cust_service_name = ""
        out_msg = wrong_cust_service_message
        
        return cust_service_status,cust_service_id,cust_service_name,out_msg

    found = 0
    selected_option = {}
    
    for option in cust_responses["service_dict"]:
        if str(cust_service_menu_int) == option:
            found = 1
            cust_service_id = cust_responses["service_dict"][option]["id"]
            cust_service_name = cust_responses["service_dict"][option]["name"]
            break

    if found == 0:
        cust_service_status = 0
        out_msg = wrong_cust_sub_service_message

    elif found == 1:
        cust_service_status = 1
        out_msg = all_okay_message

    return cust_service_status,cust_service_id,cust_service_name,out_msg


def check_sub_service(cust_sub_service_menu_int,cust_responses):
    print("Check Sub Service Function")
    print("cust_sub_service_menu_int")
    print(cust_sub_service_menu_int)
     
    cust_sub_service_status = 0
    try:
        cust_sub_service_menu_int = int(cust_sub_service_menu_int)
    except:
        ss_status = 0
        ss_id = 0
        ss_name = "" 
        ss_duration = 0
        ss_price = 0
        out_msg = wrong_cust_sub_service_message
        return ss_status,ss_id,ss_name,ss_duration,ss_price,out_msg
    
    print("Done with try catch") 
    found = 0
    selected_option = {}
    print("ssdict")
    print(cust_responses["sub_service_dict"])

    
    for option in cust_responses["sub_service_dict"]:
        print("HHH")
        print(option)
        print(cust_sub_service_menu_int)
        if str(cust_sub_service_menu_int) == option:
            print("found")
            found = 1
            ss_id = cust_responses["sub_service_dict"][option]["id"]
            ss_name = cust_responses["sub_service_dict"][option]["item"]
            ss_duration = cust_responses["sub_service_dict"][option]["duration"]
            ss_price = cust_responses["sub_service_dict"][option]["price"]
            break
        else:
            print("not found")
            ss_id = 0
            ss_name = "" 
            ss_duration = 0 
            ss_price = ""

    if found == 0:
        print("I am not found")
        ss_status = 0
        out_msg = wrong_cust_sub_service_message

    elif found == 1:
        print("I am found")
        ss_status = 1
        out_msg = all_okay_message
    
    
    return ss_status,ss_id,ss_name,ss_duration,ss_price,out_msg

def check_avail_options(cust_avail_options_menu_int, avail_display_options):
    cust_avail_options_status = 0
    try:
        cust_avail_options_menu_int = int(cust_avail_options_menu_int)
    except:
        cust_avail_options_status = 0
        cust_avail_options_response = None
        out_msg = wrong_cust_avail_options_message
        return cust_avail_options_status, cust_avail_options_response, out_msg

    #avail_options_id = avail_options_menu_int_to_id(cust_avail_options_menu_int)
    found = 0
    selected_option = [0,0,0]
    print("HELLO")
    for option in avail_display_options:
        print(option)
        print(option[0])
        if cust_avail_options_menu_int == option[0]:
            found = 1
            selected_option = option
            break # This works without "break" only because I have not added ELSE part

    if found == 0:
        cust_avail_options_status = 0
        cust_avail_options_response = None
        out_msg = wrong_cust_avail_options_message

    elif found == 1:
        cust_avail_options_status = 1
        cust_avail_options_response = selected_option
        out_msg = all_okay_message

    return cust_avail_options_status, selected_option, out_msg



def check_phone(phone):
    phone_status = 0
    if not phone:
        phone_status = 0
        return phone_status, empty_phone_message
    else:
        phone_status = 1
        return phone_status, all_okay_message

def check_color(color_menu_int):
    print("ColorMenuInt: " + str(color_menu_int))
    print("Inside CheckColor")
    color_status = 0
    if not color_menu_int:
        print("Inside NotColorMenuInt")
        color_status = 0
        color_response = 0
        color_idea = 0
        return color_status, color_response, color_idea, wrong_color_message
    else:
        print("Inside Else")
        color_name = color_menu_int_to_name(color_menu_int)
        print("ColorName: " + str(color_name))
        if color_name == "nothing":
            print("Inside ColorNameNothing")
            color_status = 0
            color_response = 0
            color_idea = 0
            return color_status, color_response, color_idea, wrong_color_message
        else:
            print("Inside Inner Else")
            color_status = 1
            color_response = color_name
            color_idea = color_menu_int_to_idea(color_menu_int)
        print("All Okay")
    return color_status, color_response, color_idea, all_okay_message


"""
def check_service(service_inp):
service_status = 0
service_name = "nothing"
service_int = None

try:
service_int = int(service_inp)
except:
service_status = 0
return service_status, wrong_service_message

service_name = service_numbers_to_strings(service_int)

if service_name == "nothing":
service_status = 0
return service_int, service_status, wrong_service_message
else:
service_status = 1
return service_int, service_status, good_service_message
"""

def check_date(date_inp):
    date_status = 0
    date_obj = None

    try:
        date_obj = datetime.datetime.strptime(date_inp, '%d-%m-%Y')
    except:
        date_status = 0
        return date_obj, date_status, wrong_date_message

    if date_obj is None:
        date_status = 0
        return date_obj, date_status, wrong_date_message
    else:
        date_status = 1
        return date_obj, date_status, all_okay_message



def check_time(time_inp):
    time_status = 0
    dummy_time_inp = "01-01-2000 " + time_inp
    time_obj = None

    try:
        time_obj = datetime.datetime.strptime(dummy_time_inp, '%d-%m-%Y %H:%M')
        print("Time Obj: " + str(time_obj))
    except:
        time_status = 0
        return time_obj, time_status, wrong_time_message

    if time_obj is None:
        time_status = 0
        return time_obj, time_status, wrong_time_message
    else:
        time_status = 1
        return time_obj, time_status, good_time_message


def old_ask_date():
    date_str = input(get_date_message)
    date_obj = None

    while date_obj is None:

        try:
            date_obj = datetime.datetime.strptime(date_str, '%d-%m-%Y')
    #print ("DateObject:" + str(date_obj))
        except:
            #print(wrong_date_message)
            date_str = input(wrong_date_message)
        return date_obj



def ask_time():
    time_str = input(get_time_message)
    dummy_time_str = "01-01-2000 " + time_str

    time_obj = None

    while time_obj is None:

        try:
            time_obj = datetime.datetime.strptime(dummy_time_str, '%d-%m-%Y %H:%M')
    #print ("DateTimeObject:" + str(date_time_obj))
        except:
            #print(wrong_date_message)
            time_str = input(wrong_time_message)
            dummy_time_str = "01-01-2000 " + time_str
    return time_obj

def calc_date_time(date_obj,time_obj):
    inp_hour = time_obj.hour
    inp_minute = time_obj.minute
    date_time_obj = date_obj.replace(hour=inp_hour, minute=inp_minute)
    return date_time_obj

##########################################################################
###### CHAT BOT VARIABLES END HERE
##########################################################################





# Preparing the Classifier
#monthwise

cur_dir = os.path.dirname('__file__')

#total sales
#monthwise
regressor = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelmonths.pkl'), 'rb'))
model_colm = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsm.pkl'),'rb')) 

#daywise
clf = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modeldays.pkl'), 'rb'))
model_cold = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsd.pkl'),'rb')) 

#weekwise
clfweek = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelweeks.pkl'), 'rb'))
model_colw = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsw.pkl'),'rb')) 



#customer visits
#daywise
clfvd = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelvdays.pkl'), 'rb'))
model_colvd = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsvd.pkl'),'rb')) 


#monthwise
clfvm = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelvmonths.pkl'), 'rb'))
model_colvm = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsvm.pkl'),'rb')) 

#weekwise
clfvw = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/modelvweeks.pkl'), 'rb'))
model_colvw = pickle.load(open(os.path.join(cur_dir,
    'pkl_objects/model_columnsvw.pkl'),'rb')) 


#expenses monthwise
regressor_exp = pickle.load(open(os.path.join(cur_dir,
                'pkl_objects/modelexm.pkl'), 'rb'))
model_colexp = pickle.load(open(os.path.join(cur_dir,
                'pkl_objects/model_columnsexm.pkl'),'rb'))


# Your API definition
app = Flask(__name__)
#app.secret_key = os.urandom(24)



#for localhost
cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})

#daywise
@app.route('/day', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

#for gcp cloud
#cors = CORS(app, resources={r"/": {"origins": "https://jts-board.appspot.com/"}})

#@app.route('/', methods=['POST'])
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])

def predict():
#print(request)
    if clf:
        try:
            print("LLLLLLLLLLLLLLL")
            jsond = request.json
            queryd = pd.get_dummies(pd.DataFrame(jsond))
            queryd = queryd.reindex(columns=model_cold, fill_value=0)
            
            predictiond = list(clf.predict(queryd).astype("int64"))
            print(predictiond)
            


            print(queryd)
            copy_queryd = queryd.copy(deep=True)
            copy_queryd.columns = ['day','month','year']

            date_time = pd.to_datetime(copy_queryd[['day', 'month', 'year']])
            #date_time.columns = ['timestamp']

            date_time_df=pd.DataFrame(date_time, columns=["timestamp"])
            date_time_df['day'] = date_time_df['timestamp'].dt.dayofweek
            dnum=pd.DataFrame(date_time_df['day'])
            dname = dnum['day'].apply(lambda x: calendar.day_abbr[x])
            #df['weekday'] = df['Timestamp'].apply(lambda x: x.weekday())
            
            print("PPPPPPPPPPPPPP")
            #print(copy_queryd)
            #print(date_time_df)
            #print(dname)
            print("JJJJJJJJJJJJJJ")

            #print(queryd['m'])
            #mname = queryd['d'].apply(lambda x: calendar.day_abbr[x])
            #print(mname)
            #print(queryxid1)

            #mname=pd.DataFrame(queryd['d'])
            #mname=pd.DataFrame(mname)

            predictiond=pd.DataFrame(predictiond, columns=["sales"])
            predictiond['sales'] = predictiond['sales'].apply(lambda x: x/1000)

            print(predictiond)
            con=pd.concat([dname,predictiond], axis=1)##################
            print(con)
            df=pd.DataFrame(con)###############


            df.set_index('day')['sales'].to_dict()
            print(df)

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            days = df['day'].tolist()
            sales = df['sales'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=days[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")



            a = "cheese"
            return json_dict
            #return jsonify({'prediction': str(predictiond)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise
@app.route('/month', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonth():
    #print(request)
    if regressor:
        try:
            json1= request.json
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colm, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'


            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor.predict(query1).astype('int64'))
            #print(prediction1)
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["sales"])
            
            prediction1['sales'] = prediction1['sales'].apply(lambda x: x/1000)

            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            months = df['month'].tolist()
            sales = df['sales'].tolist()

            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")


            #dict(zip(df.m, df.s))
            
            #from collections import defaultdict
            #mydict = defaultdict(list)
            #for k, v in zip(df.m.values,df.s.values):
            #    mydict[k].append(v)
            #    mydict[k]="x"
            #    mydict[v]="v"

            
            #print("LLLLLLLLLLOOO")
            #print(mydict)
            #print(k)
            #print(v)
            #print("LLLLLLLLLL")
            
            #df.groupby('name')[['value1','value2']].apply(lambda g: g.values.tolist()).to_dict()

            
            
            #return jsonify({'prediction': str(prediction1)})
            #t = "cheese"
            #return(t)
            return(json_dict)

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#weekwise
@app.route('/week', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predweek():
    #print(request)
    if clfweek:
        try:
            print("WWWWWWWWWWWWWWWWWWWWWWWWW")
            jsonw= request.json
            queryw = pd.get_dummies(pd.DataFrame(jsonw))
            queryw = queryw.reindex(columns=model_colw, fill_value=0)


            print(queryw)
            print("OOOOOOOOOOOOOOOOO")
            #print(query1['m'])
            #mname = queryw['w'].apply(lambda x: calendar.day_abbr[x])########
            #print(mname)
            #print(query1)
            mname=pd.DataFrame(queryw['week'])#########
            print(mname)
            print("WWWWWWWWWWWWWWWWWWWWWw")

            
            predictionw = (clfweek.predict(queryw).astype("int64"))
            
            #print("PPPPPPPPPPPPPP")
            #print(predictionw)
            #print("JJJJJJJJJJJJJJ")

            #print(prediction1)
            #print(prediction)
            predictionw=pd.DataFrame(predictionw, columns=["sales"])##########
            print(predictionw)
            predictionw['sales'] = predictionw['sales'].apply(lambda x: x/1000)

            con=pd.concat([mname,predictionw], axis=1)##################
            print(con)
            df=pd.DataFrame(con)################


            df.set_index('week')['sales'].to_dict()
            #print(df)



            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            weeks = df['week'].tolist()
            sales = df['sales'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=weeks[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            return json_dict
            #return jsonify({'prediction weekwise': str(predictionw).splitlines()})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


#customer visits  
#daywise
@app.route('/vdays', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

#for gcp cloud
#cors = CORS(app, resources={r"/": {"origins": "https://jts-board.appspot.com/"}})

#@app.route('/', methods=['POST'])
#@cross_origin(origin='*',headers=['Content- Type','Authorization'])

def predictvdays():
    #print(request)
    if clfvd:
        try:
           # print("LLLLLLLLLLLLLLL")
            jsond = request.json
            queryd = pd.get_dummies(pd.DataFrame(jsond))
            queryd = queryd.reindex(columns=model_colvd, fill_value=0)
            
            predictiond = list(clfvd.predict(queryd))
            #print(predictiond)
            


            #print(queryd)
            copy_queryd = queryd.copy(deep=True)
            copy_queryd.columns = ['day','month','year']

            date_time = pd.to_datetime(copy_queryd[['day', 'month', 'year']])
            #date_time.columns = ['timestamp']

            date_time_df=pd.DataFrame(date_time, columns=["timestamp"])
            date_time_df['day'] = date_time_df['timestamp'].dt.dayofweek
            dnum=pd.DataFrame(date_time_df['day'])
            dname = dnum['day'].apply(lambda x: calendar.day_abbr[x])
            #df['weekday'] = df['Timestamp'].apply(lambda x: x.weekday())
            
            #print("PPPPPPPPPPPPPP")
            #print(copy_queryd)
            #print(date_time_df)
            #print(dname)
            #print("JJJJJJJJJJJJJJ")

            #print(queryd['m'])
            #mname = queryd['d'].apply(lambda x: calendar.day_abbr[x])
            #print(mname)
            #print(queryxid1)

            #mname=pd.DataFrame(queryd['d'])
            #mname=pd.DataFrame(mname)

            predictiond=pd.DataFrame(predictiond, columns=["visits"])
            #predictiond[''] = predictiond['s'].apply(lambda x: x/1000)

            #print(predictiond)
            con=pd.concat([dname,predictiond], axis=1)##################
            #print(con)
            df=pd.DataFrame(con)###############


            df.set_index('day')['visits'].to_dict()
            #print(df)

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            days = df['day'].tolist()
            sales = df['visits'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=days[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            """
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")
            """











            a = "cheese"
            return json_dict
            #return jsonify({'prediction': str(predictiond)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')



#monthwise

#monthwise
@app.route('/vmonths', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predvmonths():
    #print(request)
    if clfvm:
        try:
            json1= request.json
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colvm, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            

            """print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            """
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            #print(mname)
            
            prediction1 = (clfvm.predict(query1))
            #print(prediction1)
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["visits"])
            
            #prediction1['visits'] = prediction1['s'].apply(lambda x: x/1000)

            con=pd.concat([mname,prediction1], axis=1)
            """print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")"""
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['visits'].to_dict()

            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            months = df['month'].tolist()
            sales = df['visits'].tolist()

            """print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")"""

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            """print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")"""

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)

            # the result is a JSON string:
            """print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")"""


            #dict(zip(df.m, df.s))
            
            #from collections import defaultdict
            #mydict = defaultdict(list)
            #for k, v in zip(df.m.values,df.s.values):
            #    mydict[k].append(v)
            #    mydict[k]="x"
            #    mydict[v]="v"

            
            #print("LLLLLLLLLLOOO")
            #print(mydict)
            #print(k)
            #print(v)
            #print("LLLLLLLLLL")
            
            #df.groupby('name')[['value1','value2']].apply(lambda g: g.values.tolist()).to_dict()

            
            
            #return jsonify({'prediction': str(prediction1)})
            #t = "cheese"
            #return(t)
            return(json_dict)
    
        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')



#weekwise
@app.route('/vweeks', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predvweeks():
    #print(request)
    if clfvw:
        try:
            print("WWWWWWWWWWWWWWWWWWWWWWWWW")
            jsonw= request.json
            queryw = pd.get_dummies(pd.DataFrame(jsonw))
            queryw = queryw.reindex(columns=model_colvw, fill_value=0)


            print(queryw)
            print("OOOOOOOOOOOOOOOOO")
            #print(query1['m'])
            #mname = queryw['w'].apply(lambda x: calendar.day_abbr[x])########
            #print(mname)
            #print(query1)
            mname=pd.DataFrame(queryw['week'])#########
            print(mname)
            print("WWWWWWWWWWWWWWWWWWWWWw")

            
            predictionw = (clfvw.predict(queryw).astype("int64"))
            
            #print("PPPPPPPPPPPPPP")
            #print(predictionw)
            #print("JJJJJJJJJJJJJJ")

            #print(prediction1)
            #print(prediction)
            predictionw=pd.DataFrame(predictionw, columns=["visits"])##########
            print(predictionw)
            predictionw['visits'] = predictionw['visits'].apply(lambda x: x/1000)

            con=pd.concat([mname,predictionw], axis=1)##################
            print(con)
            df=pd.DataFrame(con)################


            df.set_index('week')['visits'].to_dict()
            #print(df)



            count = df.shape[0]
            #print(count)

            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")


            weeks = df['week'].tolist()
            sales = df['visits'].tolist()

            #print("LLLLLLLLLLOOO")
            #print(months[1])
            #print(sales[1])
            #print("KKKKKKKKKKKKK")

            list_of_dicts = []
            D={}

            #add a key and setup for a sub-dictionary

            for i in range(count):
                D[i] = {}
                D[i]['x']=weeks[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])


            #print(list_of_dicts)

            # convert into JSON:
            json_dict = json.dumps(list_of_dicts)

            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            return json_dict
            #return jsonify({'prediction weekwise': str(predictionw).splitlines()})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')


#monthwise expenses

@app.route('/monthexp', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonthexp():
    #print(request)
    if regressor_exp:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colexp, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)

            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor_exp.predict(query1).astype('int64'))

            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["expenses"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['expenses'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            #months = df['month'].tolist()
            expenses = df['expenses'].tolist()
            
            
            ###################################################################
            
            
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            

            copy_query2 = query2.copy(deep=True)
            copy_query2['month'] = copy_query2['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query2['month']
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            sales_npar = np.asarray(sales)
            expenses_npar = np.asarray(expenses)
            profit_npar = sales_npar - expenses_npar
            profit = profit_npar.tolist()
            
            #profit = sales - expenses
            print("NNNNNNNNNNNNN")
            print(sales)
            print(expenses)
            print(profit)
            print("KKKKKKKKKKKKK")
            
            
            
            
            ################################################################
            
            join = list(zip(months,sales,expenses,profit))  ###################
            join_json_string = json.dumps(join,ensure_ascii=False)
            

            
            '''
            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")
            
            list_of_dicts = []
            D={}
            
            #add a key and setup for a sub-dictionary
            
            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")
            
            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)
            
            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            '''
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(join_json_string)

        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise donut
@app.route('/monthexpdonut', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def predmonth_expdonut():
    #print(request)
    if regressor_exp:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colexp, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor_exp.predict(query1).astype('int64'))
            
            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["expenses"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['expenses'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            #months = df['month'].tolist()
            expenses = df['expenses'].tolist()
            
            
            ###################################################################
            
            
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            copy_query2 = query2.copy(deep=True)
            copy_query2['month'] = copy_query2['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query2['month']
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            sales_npar = np.asarray(sales)
            expenses_npar = np.asarray(expenses)
            profit_npar = sales_npar - expenses_npar
            profit = profit_npar.tolist()
            
            list_of_dicts = []
            D = {}
            D['x']="利益"
            D['value']=profit[0]
            list_of_dicts.append(D)
            
            E = {}
            E['x']="費用"
            E['value']=expenses[0]
            list_of_dicts.append(E)
            
            #list_of_dicts.append(D[i])
            
            #list_output = [['Expenses', expenses[0]],['Saving', profit[0]]]
            #profit = sales - expenses
            print("NNNNNNNNNNNNN")
            #print(sales[0])
            print(expenses[0])
            print(profit[0])
            print(list_of_dicts)
            print("KKKKKKKKKKKKK")
            
            
            ################################################################
            
            #out_json_string = json.dumps(list_output,ensure_ascii=False)
            out_json_string = json.dumps(list_of_dicts,ensure_ascii=False)
            
            
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(out_json_string)

        except:
    
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#monthwise column
@app.route('/monthexpcolumn', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

def predmonth_expcolumn():
    #print(request)
    if regressor_exp:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colexp, fill_value=0)
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            print("JJJJJJJJJJJJJJJJJJ")
            print(query1)
            print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (regressor_exp.predict(query1).astype('int64'))
            
            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["expenses"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['expenses'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            #months = df['month'].tolist()
            expenses = df['expenses'].tolist()
            
            
            ###################################################################
            
            
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            copy_query2 = query2.copy(deep=True)
            copy_query2['month'] = copy_query2['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query2['month']
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            sales_npar = np.asarray(sales)
            expenses_npar = np.asarray(expenses)
            profit_npar = sales_npar - expenses_npar
            profit = profit_npar.tolist()
            
            #list_of_dicts = []
            #D = {}
            #D['x']="Saving"
            #D['value']=profit[0]
            #list_of_dicts.append(D)
            
            #E = {}
            #E['x']="Expenses"
            #E['value']=expenses[0]
            #list_of_dicts.append(E)
            
            list_output = [['売上', sales[0]],['費用', expenses[0]]]

            print("NNNNNNNNNNNNN")
            #print(sales[0])
            print(expenses[0])
            print(profit[0])
            print("KKKKKKKKKKKKK")
            
            
            ################################################################
            
            out_json_string = json.dumps(list_output,ensure_ascii=False)
            #out_json_string = json.dumps(list_of_dicts,ensure_ascii=Fa1lse)
            
            
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(out_json_string)

        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')




#monthwise
@app.route('/monthv', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def predmonv():
    #print(request)
    if clfvm:
        try:
            print("HELLLO")
            json1= request.json
            length = len(json1)
            
            
            
            query1 = pd.get_dummies(pd.DataFrame(json1))
            query1 = query1.reindex(columns=model_colvm, fill_value=0)
            
            #mname = query1['month'].apply(lambda x: calendar.month_abbr[x])
            
            #print(query1)
            copy_query1 = query1.copy(deep=True)
            copy_query1['month'] = copy_query1['month'].astype(str) + '月'
            
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query1)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            #mname = query1['m'].apply(lambda x: calendar.month_abbr[x])
            mname = copy_query1['month']
            #print(mname)
            #print(query1)
            
            mname=pd.DataFrame(mname)
            print(mname)
            
            prediction1 = (clfvm.predict(query1).astype('int64'))

            print("JJJJJJJJJJ")
            print(prediction1)
            print("KkKKKKKK")
            #print(prediction)
            prediction1=pd.DataFrame(prediction1, columns=["visits"])
            
            #prediction1['expenses'] = prediction1['expenses'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction1], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['visits'].to_dict()
            
            count = df.shape[0]
            #print(count)
            
            #print("LLLLLLLLLLOOO")
            #print(df)
            #print("KKKKKKKKKKKKK")
            
            
            months = df['month'].tolist()
            visits = df['visits'].tolist()
            
            
            ###################################################################
            
            """
            
            query2 = pd.get_dummies(pd.DataFrame(json1))
            query2 = query2.reindex(columns=model_colm, fill_value=0)
            
            #print("JJJJJJJJJJJJJJJJJJ")
            #print(query2)
            #print("SSSSSSSSSSSSSSSSSS")
            
            
            mname = query2['month'].apply(lambda x: calendar.month_abbr[x])
            mname=pd.DataFrame(mname)
            
            
            prediction2 = (regressor.predict(query2).astype('int64'))
            prediction2=pd.DataFrame(prediction2, columns=["sales"])
            
            #prediction2['sales'] = prediction2['sales'].apply(lambda x: x/1000)
            
            con=pd.concat([mname,prediction2], axis=1)
            print("IIIIIIIIIII")
            print(con)
            print("NNNNNNNNNN")
            df=pd.DataFrame(con)
            #df.set_index('m')['0'].to_dict()
            df.set_index('month')['sales'].to_dict()
            
            count = df.shape[0]
            #print(count)
            months = df['month'].tolist() ########################
            sales = df['sales'].tolist() ##########################
            
            
            
            
            ################################################################
            """
            
            join = list(zip(months, visits))  ###################
            
            join_json_string = json.dumps(join,ensure_ascii=False)
            

            
            '''
            print("PPPPPPPPPP")
            print(months)
            print(sales)
            print("KKKKKKKKKKKKK")
            
            list_of_dicts = []
            D={}
            
            #add a key and setup for a sub-dictionary
            
            for i in range(count):
                D[i] = {}
                D[i]['x']=months[i]
                D[i]['value']=sales[i]
                list_of_dicts.append(D[i])

            print("BBBBBBBBBBBBBB")
            print(list_of_dicts)
            print("LLLLLLLLLLLLLL")
            
            # convert into JSON:
            json_dict = json.dumps(list_of_dicts,ensure_ascii=False)
            
            # the result is a JSON string:
            print("LLLLLLLLLLOOO")
            print(json_dict)
            print("KKKKKKKKKKKKK")

            '''
            
            
            #t = "cheese"
            #return(t)
            #return(json_dict)
            return(join_json_string)

        except:
        
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#####################################################################
#####  CHAT BOT API
#####################################################################

# PROGRAM STARTS HERE


@app.route('/dropsession', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


def dropsession():
    json_input = request.json
    ip = json_input['ip']
    print("IP:",ip)

    sql = "DELETE FROM sessions WHERE ip = %s"
    delete_tuple = (ip,)
    mycursor.execute(sql,delete_tuple)
    mydb.commit()
    #DELETE FROM table_name WHERE condition;
    return "dropped\n"



@app.route('/chat', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])



def chat():


    print("START")
    print("I am inside chat method")
    #if 'user' not in session:
    #    return "yes are not logged in"
    print("Inside CHAT")
    #print("Session", session)
    #print(session["STATE"])

    json_input = request.json

    ip = json_input['ip']
    inp_msg  = json_input['message']
    user_id = json_input['user']

    print("\n\n\n\n\n\n\n\n")
    print(ip)
    print("\n\n\n\n\n\n\n\n")
    
    sql = """select * from sessions where ip = %s """
    data = (ip,)
    mycursor.execute(sql,data)

    myresult_list = mycursor.fetchall()
    #emp_name_dict = dict()

    print("Myresult",type(myresult_list),"List")
    #print(myresult_list)
    #return "nothing"

    if len(myresult_list) != 0:
        print("matched")
        #myfirst_tuple = None
        myfirst_tuple = myresult_list[0]
        #if myfirst_tuple is not None:
        ip= myfirst_tuple[0]
        #cust_name= myfirst_tuple[1]
        #is_nickname= myfirst_tuple[2]
        #cust_nickname= myfirst_tuple[3]
        #cust_birthday= myfirst_tuple[4]
        #cust_phone= myfirst_tuple[5]
        #cust_is_time_for_more= myfirst_tuple[6]
        #cust_color= myfirst_tuple[7]
        #cust_type_of_salon= myfirst_tuple[8]
        #cust_is_reservation_now= myfirst_tuple[9]
        #cust_date= myfirst_tuple[10]
        #cust_service_id= myfirst_tuple[11]
        #cust_avail_msg=myfirst_tuple[12]
        #cust_avail_display_options= myfirst_tuple[13]
        #cust_avail_display_options = list(cust_avail_display_options)
        #cust_avail_option_list= myfirst_tuple[14]
        #cust_avail_option_list = list(cust_avail_option_list)



        print("\n\n\n I am here1 \n\n\n")
        return_list_of_dicts = []
        
        return_list_of_dicts_1= myfirst_tuple[15]
        #return_list_of_dicts_proc=list(return_list_of_dicts_proc)

        print("\n\n\nReturn List OF Dicts PROC\n\n\n")
        #print(return_list_of_dicts_1)
        #print(type(return_list_of_dicts_1))

        return_list_of_dicts_2 = return_list_of_dicts_1.replace("'", "\"")
        #print(return_list_of_dicts_2) 
        
        return_list_of_dicts = json.loads(return_list_of_dicts_2)
        #return_list_of_dicts = json.loads(return_list_of_dicts_1)
        #return "nothing"
         
        #print(return_list_of_dicts)
        #print(type(return_list_of_dicts))

        print("\n\n\n I am here2 \n\n\n")
        #count = 0


        #return "nothing"
        """
        for dict_str in return_list_of_dicts_3:
            #if count > 1:
            print("\n\n\n Inside For \n\n\n") 
            print(dict_str)
            print(type(dict_str))
             
            print("\n\n\n I am inside \n\n\n")
            accept_str = dict_str.replace("'", "\"")
            print("\n\n\n I am inside2 \n\n\n")
            print("accept",accept_str,"str")
            return_dict = json.loads(accept_str)
            print("\n\n\n I am inside3 \n\n\n")
            return_list_of_dicts.append(return_dict)
            #count += 1
        """
        #cust_duration= myfirst_tuple[16]
        STATE= myfirst_tuple[17]

        return_dict_str= myfirst_tuple[18]
        return_dict_accept_str = return_dict_str.replace("'", "\"")
        return_dict = json.loads(return_dict_accept_str)
        print("here2.5")
        cust_responses_str= myfirst_tuple[19]
        cust_responses_accept_str = cust_responses_str.replace("'", "\"")


        print("cust responses acc\n")
        #print(cust_responses_accept_str)
        print("\ncust responses acc\n")


        cust_responses = json.loads(cust_responses_accept_str)
        print("here3")
        #return_dict= dict(return_dict)
        #print(session)
        #return "hello"
    else:
        print("unmatched")
        STATE= "WELCOME_ASK_NAME"
        cust_name= ""
        is_nickname= ""
        cust_nickname= ""
        cust_birthday= ""
        is_time_for_more= ""
        cust_phone= ""
        cust_color= ""
        cust_type_of_salon= ""
        is_reservation_now= ""
        cust_date_obj= ""
        cust_service_id= ""
        cust_avail_msg= ""
        cust_avail_display_options= []
        cust_avail_option_list= []
        cust_responses= {}
        return_list_of_dicts= []
        return_dict= {}
        duration= 2



    print("Return Dicts")
    #print(type(return_dict))
    #return "okay"

    #print(type(cust_avail_display_options))
    #print(type(cust_avail_option_list))
    #print(type(return_list_of_dicts))

    #return("okay")
    #if 'user' not in session:
    #    return "yes are not logged in"
    print("Inside CHAT")
    #print("Session", session)
    print(STATE)
    print("LLLLLLLLLLLLLLLLLLLLLLLLLL")
    #return "nothing"

    if inp_msg == "init" and STATE != "WELCOME_ASK_NAME":
        
        if STATE == "IS_RESERVATION_NOW":
            out_msg,option_list = is_reservation_now_fun()
            STATE = "IS_RESERVATION_NOW_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
        else:
            print("ReturnDict")
            #print(return_dict)

            if return_dict["status"] == "failure":
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""   
            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json

    while True:

        if STATE == "WELCOME_ASK_NAME":
            out_msg = welcome_ask_name()
            STATE = "NAME_ASKED"

            out_dict = {"type" : "input", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            insert_into_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            out_json = json.dumps(return_dict,ensure_ascii= False)
            return out_json
         
        if STATE == "NAME_ASKED":
            cust_name = inp_msg
            name_st,out_msg = check_name(cust_name)
            if name_st == 1:
                cust_responses["name"] = cust_name

                return_dict["status"] = "success"
                return_dict["status"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {"type": "text", "answer": cust_name}
                return_list_of_dicts.append(out_dict)

                
                STATE = "IS_NICKNAME"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_NICKNAME":
            out_msg,option_list = is_nickname_fun()
            STATE = "IS_NICKNAME_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json


        if STATE == "IS_NICKNAME_ASKED":
            is_nickname_menu_int = inp_msg
            
            is_nickname_status,is_nickname_response,out_msg = check_is_nickname(is_nickname_menu_int)
            
            if is_nickname_status == 1:
                cust_responses["is_nickname"] = is_nickname_response
            
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts

                out_dict = {"type": "text", "answer": is_nickname_response}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                if is_nickname_response == "yes":
                    STATE = "ASK_NICKNAME"
                elif is_nickname_response == "no":
                    STATE = "ASK_BIRTHDAY"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_NICKNAME":
            print("JJJJJ")
            out_msg = ask_nickname()
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            
            out_dict = {"type" : "input", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            STATE = "NICKNAME_ASKED"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)

            #time.sleep(2) 
            return out_json

        if STATE == "NICKNAME_ASKED":
            print("KKKKKK")
            cust_nickname = inp_msg
            nickname_status,out_msg = check_name(cust_nickname)
            if nickname_status == 1:
                cust_responses["nickname"] = cust_nickname
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_nickname}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_BIRTHDAY"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_BIRTHDAY":
            out_msg = ask_birthday(cust_responses)
            STATE = "BIRTHDAY_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            out_json = json.dumps(return_dict,ensure_ascii= False)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            #time.sleep(2) 
            return out_json

        if STATE == "BIRTHDAY_ASKED":
            cust_birthday = inp_msg
            birthday_obj,birthday_status,out_msg = check_date(cust_birthday)
            birthday_str = str(birthday_obj)
            if birthday_status == 1:
                cust_responses["birthday"] = birthday_str
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "status": "success", "answer": birthday_str}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_PHONE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_PHONE":
            out_msg = ask_phone()
            STATE = "PHONE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "input", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "PHONE_ASKED":
            cust_phone = inp_msg
            phone_status,out_msg = check_phone(cust_phone)
            if phone_status == 1:
                cust_responses["phone"] = cust_phone
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_phone}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "IS_TIME_FOR_MORE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_TIME_FOR_MORE":
            out_msg,option_list = is_time_for_more_fun()
            STATE = "IS_TIME_FOR_MORE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "IS_TIME_FOR_MORE_ASKED":
            is_time_for_more_menu_int = inp_msg
            is_time_for_more_status,is_time_for_more_response,out_msg = check_is_time_for_more(is_time_for_more_menu_int)
            if is_time_for_more_status == 1:
                cust_responses["is_time_for_more"] = is_time_for_more_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "status":"success", "answer": is_time_for_more_response}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if is_time_for_more_response == "yes":
                    STATE = "ASK_COLOR"
                elif is_time_for_more_response == "no":
                    STATE = "IS_RESERVATION_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_COLOR":
            out_msg, option_list = ask_color(cust_responses)
            STATE = "COLOR_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts

            out_dict = {"type" : "option", "question": out_msg,"option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "COLOR_ASKED":
            cust_color = inp_msg
            
            color_status,color_response,color_idea,out_msg = check_color(cust_color)
            if color_status == 1:
                print("Inside ColorStatus 1")
                color_idea = color_idea
                cust_responses["color"] = color_response
                cust_responses["color_idea"] = color_idea
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": color_response}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_TYPE_OF_SALON"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                print("ColorStatusnot1")
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_TYPE_OF_SALON":
            color_idea = cust_responses["color_idea"]
            out_msg,option_list = ask_type_of_salon(color_idea)
            STATE = "TYPE_OF_SALON_ASKED"

            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "TYPE_OF_SALON_ASKED":
            cust_type_of_salon_menu_int = inp_msg
            
            cust_type_of_salon_status,cust_type_of_salon,out_msg = check_cust_type_of_salon(cust_type_of_salon_menu_int)
            
            if cust_type_of_salon_status == 1:
                cust_responses["type_of_salon"] = cust_type_of_salon
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text","answer": cust_type_of_salon}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                STATE = "IS_RESERVATION_NOW"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_RESERVATION_NOW":
            out_msg,option_list = is_reservation_now_fun()
            STATE = "IS_RESERVATION_NOW_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json


        if STATE == "IS_RESERVATION_NOW_ASKED":
            is_reservation_now_menu_int = inp_msg
            is_reservation_now_status,is_reservation_now_response,out_msg = check_is_reservation_now(is_reservation_now_menu_int)
            if is_reservation_now_status == 1:
                cust_responses["is_reservation_now"] = is_reservation_now_response
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text", "answer": is_reservation_now_response}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if is_reservation_now_response == "yes":
                    STATE = "ASK_DATE"
                elif is_reservation_now_response == "no":
                    STATE = "GOOD_BYE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "GOOD_BYE":
            out_msg = "お話出来てよかった。 じゃあまたね。/ Nice talking to you. See You Later."
            out_dict = {"type" : "text", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            STATE = "IS_RESERVATION_NOW"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json
        
        if STATE == "ASK_DATE":
            out_msg = ask_date()
            STATE = "DATE_ASKED"
            out_dict = {"type" : "input", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            time.sleep(2) 
            return out_json



        if STATE == "DATE_ASKED":
            print("Inside Date Asked")
            cust_date = inp_msg
            cust_date_obj,cust_date_status,out_msg = check_date(cust_date)
            cust_date_str = str(cust_date_obj)
            if cust_date_status == 1:
                cust_responses["date"] = cust_date_str
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text","answer": cust_date_str}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                STATE = "ASK_SERVICE"
                
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json


        if STATE == "ASK_SERVICE":
            out_msg,option_list,service_dict = ask_service_fun(user_id)
            STATE = "SERVICE_ASKED"
            cust_responses["service_dict"] = service_dict
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json



        if STATE == "SERVICE_ASKED":
            cust_service_menu_int = inp_msg
            serv_status,serv_id,serv_name,out_msg =check_service(cust_service_menu_int,cust_responses)
            
            if serv_status == 1:
                cust_responses["service"] = serv_id
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                #if cust_service_id == 1:
                #    cust_service_name = "ネイル / Nail"
                #elif cust_service_id == 2:
                #    cust_service_name = "エステ / Aesthetic"

                out_dict = {"type" : "text", "answer": serv_name, "id": serv_id }
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                sub_service_dict = get_sub_services(serv_id,user_id)
                cust_responses["sub_service_dict"] = sub_service_dict
                
                STATE = "ASK_SUB_SERVICE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ASK_SUB_SERVICE":
            
            out_msg,option_list = ask_sub_service_fun(cust_responses)

            STATE = "SUB_SERVICE_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "SUB_SERVICE_ASKED":
            print("sub service asked") 
            #print(cust_responses)
            
            ss_menu_int = inp_msg
            ss_status,ss_id,ss_name,ss_dur,cust_price,out_msg = check_sub_service(ss_menu_int,cust_responses)
            #print("\n\n\n\n\n CHECK SUB SERVICE ENDS \n\n\n\n\n\n\n\n") 
            
            print("ss_dur")
            print(ss_dur)
            
            if ss_status == 1:
                
                cust_responses["sub_service"] = ss_id
                cust_responses["duration"] = ss_dur
                cust_responses["price"] = cust_price
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                
                out_dict = {"type" : "text", "answer": ss_name,"id":ss_id}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"
                
                print("cust_responses[service]")
                print(cust_responses["service"])
                
                relevant_employee_list = find_employees_for_service(cust_responses["service"],user_id)
                #return "nothing"
                duration_in_hours = int(int(ss_dur) / 60)
                #duration = 2
                print("ss_dur,duration_in_hours")
                print(ss_dur,duration_in_hours)
                #return "nothing"

                cust_date_str = cust_responses["date"]
                cust_date_obj = datetime.datetime.strptime(cust_date_str, '%Y-%m-%d %H:%M:%S')
                
                avail_emp_dict = check_new_availability(cust_date_obj,relevant_employee_list,duration_in_hours,user_id)
                #return "nothing" 
                emp_name_dict = find_employee_name(user_id)

                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")

                print("avail_emp_dict")
                print(avail_emp_dict)
                
                print("---------------------------------")
                print("---------------------------------")
                print("---------------------------------")
                
                
                cust_avail_msg, cust_avail_display_options,cust_avail_option_list = convert_avail_dict_to_display_options(avail_emp_dict,emp_name_dict)
                #return "nothing" 
                cust_responses["cust_avail_msg"] = cust_avail_msg 
                cust_responses["cust_avail_display_options"] = cust_avail_display_options 
                
                STATE = "SHOW_AVAIL_OPTIONS"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))

            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "SHOW_AVAIL_OPTIONS":
            print("Inside Show Avail Options")

            cust_avail_msg = cust_responses["cust_avail_msg"]
            print("cust_responses")
            print(cust_responses)
            
            out_msg = cust_avail_msg
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": cust_avail_option_list}
            return_list_of_dicts.append(out_dict)
            
            STATE = "AVAIL_OPTIONS_SHOWN"
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "AVAIL_OPTIONS_SHOWN":
            cust_avail_options_menu_int = inp_msg
            cust_avail_display_options = cust_responses["cust_avail_display_options"]
            print("cust_avail_display_options")
            print(cust_avail_display_options)
            cust_avail_options_status, cust_selected_option, out_msg = check_avail_options(cust_avail_options_menu_int,cust_avail_display_options)
            
            if cust_avail_options_status == 1:
                print("cust_selected_option")
                print(cust_selected_option)
                #return "nothing"
                cust_responses["avail_options"] = cust_selected_option
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts


                sel_emp = cust_selected_option[1]
                slot = cust_selected_option[2]
                select_sql = """select name from employees where id = %s"""
                select_tuple = (sel_emp,)
                mycursor.execute(select_sql,select_tuple)
                myresult_list = mycursor.fetchall()
                a1 = myresult_list[0]
                a2 = a1[0]
                sel_emp_name = a2.decode() ; sel_emp_name  
                
                sel_time = slot_list[slot]

                long_option = sel_emp_name + " at " + str(sel_time) 


                out_dict = {"type" : "text","answer": long_option}
                #out_dict = {"type" : "text","answer": cust_selected_option}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_selected_option[1] == "none":
                    STATE = "ASK_DATE"
                else: 
                    STATE = "IS_CONFIRM"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "IS_CONFIRM":
            out_msg, option_list = is_confirm()
            STATE = "IS_CONFIRM_ASKED"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "option", "question": out_msg, "option_list": option_list}
            return_list_of_dicts.append(out_dict)
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json

        if STATE == "IS_CONFIRM_ASKED":
            print("inside is confirm asked")
            cust_is_confirm_menu_int = inp_msg
            cust_is_confirm_status, cust_is_confirm_response, out_msg = check_is_confirm(cust_is_confirm_menu_int)
            
            if cust_is_confirm_status == 1:
                cust_responses["is_confirm"] = cust_is_confirm_response
                
                return_dict["status"] = "success"
                return_dict["error_msg"] = ""
                return_dict["chat"] = return_list_of_dicts
                out_dict = {"type" : "text", "answer": cust_is_confirm_response}
                return_list_of_dicts.append(out_dict)
                return_list_of_dicts[-2]["type"] = "text"

                if cust_is_confirm_response == "yes":
                    STATE = "ENTER_DB"
                elif cust_is_confirm_response == "no":
                    STATE = "ASK_DATE"
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            else:
                return_dict["status"] = "failure"
                return_dict["error_msg"] = out_msg
                return_dict["chat"] = return_list_of_dicts
                update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
                out_json = json.dumps(return_dict,ensure_ascii= False)
                return out_json

        if STATE == "ENTER_DB":
            print ("inside enter db")

            if cust_responses["is_nickname"] == "no":
                cust_responses["nickname"] = ""

            if cust_responses["is_time_for_more"] == "no":
                cust_responses["color"] = ""
                cust_responses["type_of_salon"] = ""

            if cust_responses["is_reservation_now"] == "no":
                cust_responses["date"] = ""
                cust_responses["avail_options"] = [0,0,0]
                cust_responses["service"] = 0

            cust_name = cust_responses["name"]
            cust_is_nickname = cust_responses["is_nickname"]
            cust_nickname = cust_responses["nickname"]
            cust_birthday = cust_responses["birthday"]
            cust_is_time_for_more = cust_responses["is_time_for_more"]
            cust_phone = cust_responses["phone"]
            cust_color = cust_responses["color"]
            cust_type_of_salon = cust_responses["type_of_salon"]
            cust_is_reservation_now = cust_responses["is_reservation_now"]
            cust_res_date = cust_responses["date"]
            cust_slot = cust_responses["avail_options"][2]
            cust_res_time = slot_list[cust_slot]
            cust_service_id = cust_responses["service"]
            cust_sub_service_id = cust_responses["sub_service"]
            cust_emp_id = cust_responses["avail_options"][1]
            cust_is_confirm = cust_responses["is_confirm"]
            cust_duration_in_mins = cust_responses["duration"]
            cust_price = cust_responses["price"]
            cust_last_state = STATE

            #insert_into_chats_db(user_id,ip,cust_name,cust_is_nickname,cust_nickname,cust_birthday,cust_is_time_for_more,cust_phone,cust_color,cust_type_of_salon,cust_is_reservation_now,cust_res_date,cust_res_time,cust_service_id,cust_emp_id,cust_is_confirm,cust_last_state)

             
            c_id = insert_into_customers_table(cust_name,cust_nickname,cust_birthday,cust_phone,user_id)


            i_u_id=int(user_id)
            i_c_id=c_id
            i_s_id=int(cust_service_id)
            i_ss_id=int(cust_sub_service_id)
            i_e_id=str(cust_emp_id)
            #i_s_date=str(cust_res_date)
            start_date=str(cust_res_date)
            #i_e_date=str(cust_res_date)
            end_date=str(cust_res_date)
           
            start_slot = int(cust_slot)
            start_time = slot_list[start_slot] 
            
            slots_needed = int(int(cust_duration_in_mins) / 30)
            next_slot = start_slot + slots_needed
            end_time = slot_list[next_slot]
            i_s_time=str(start_time)
            i_e_time=str(end_time)

            print("--------------------------\n\n\n\n")
            print("--------------------------\n\n\n\n")

            start_date_wo_0s = start_date[:-9] 
            end_date_wo_0s = end_date[:-9] 
            
            i_s_date=str(start_date_wo_0s)
            i_e_date=str(end_date_wo_0s)

            print("--------------------------\n\n\n\n")
            print("--------------------------\n\n\n\n")
            #return "nothing"
            
            i_total= cust_price

            insert_into_reservations_table(i_u_id,i_c_id,i_s_id,i_ss_id,i_e_id,i_s_date,i_e_date,i_s_time,i_e_time,i_total)
            
            
            out_msg = "Your booking is confirmed"
            return_dict["status"] = "success"
            return_dict["error_msg"] = ""
            return_dict["chat"] = return_list_of_dicts
            out_dict = {"type" : "text", "question": out_msg}
            return_list_of_dicts.append(out_dict)
            STATE = "IS_RESERVATION_NOW" 
            update_session_db(ip,STATE,str(return_list_of_dicts),str(return_dict),str(cust_responses))
            
            out_json = json.dumps(return_dict,ensure_ascii= False)
            #time.sleep(2) 
            return out_json
    return "Cheese"

########################################################################################
########## CHAT BOT API ENDS HERE
########################################################################################


if __name__ == '__main__':
    app.run(debug=True)
    #context = ('fullchain1.pem','privkey1.pem')
    #app.run(debug=True,host='0.0.0.0',ssl_context=context)


