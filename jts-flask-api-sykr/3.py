import datetime


def get_date_in_ddmmyyyy_format(inp_str):
    inp_str = inp_str.replace("日","")
    inp_str = inp_str.replace("月","-")
    inp_str = inp_str.replace("年","-")
    
    str_list = inp_str.split("-")
    day = str_list[2]
    month = str_list[1]
    year = str_list[0]

    if int(day) < 10:
        day = "0" + day

    if int(month) < 10:
        month = "0" + month 
    
    out_date = day + "-" + month + "-" + year
    return out_date

inp_str1 = "2019年6月21日"
#x = get_date_in_ddmmyyyy_format(inp_str1)
#print(x)

today = datetime.datetime.now()

next_seven_day_list = [today,]
for i in range(1,7):
    new= today + datetime.timedelta(days=i)
    next_seven_day_list.append(new) 

print(next_seven_day_list)




