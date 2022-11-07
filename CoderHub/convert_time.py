from datetime import datetime
from typing import List
def convert_time(time: str) -> str:
    # write your code here ^_^
    
    x = time.partition(":")
    # print(x)
    min = x[2].partition(" ")
    # print(min)

    if "pm" in x[2]: 
        # print(time)
        if int(x[0]) <= 12:
            h = int(x[0]) + 12
        # print(h)
            m = min[0]
            st = str(h)+x[1]+m 
            # print(st)
    elif "am" in x[2]:
        if int(x[0]) == 12:
            h = 0
            m= min[0]
            st = str(h)+x[1]+m
            # print(st)
        else:
            h = x[0]
            m = min[0]
            st = str(h)+x[1]+m 
            # print(st)

    else:
        if int(x[0]) > 12:
            h = int(x[0]) - 12
            m = min[0]
            st = str(h) + x[1] + m + " " + "pm"
            # print(st)
        else:
            h = int(x[0])
            m = min[0]
            st = str(h) + x[1] + m + " " + "am"
            # print(st)
    return st



    

time = '10:30 am'
print(convert_time(time))

time = '7:13 pm'
print(convert_time(time))

time = '2:00'
print(convert_time(time))

time = '12:00 am'
print(convert_time(time))

# time = '10:30 am'
# print(convert_time(time))

# time = '19:00'
# print(convert_time(time))


# from datetime import datetime

# now = datetime.now()

# print(now. strftime('%H:%M:%S')) #24-hour format.
# print(now. strftime('%I:%M:%S')) #12-hour format.
