

def timePeriod(date1, date2):
    year1 = int(date1[:4])
    year2 = int(date2[:4])
    month1 = int(date1[4:7])
    month2 = int(date2[4:7])
    day1 = date1[8:10]
    day2 = date2[8:10]
    print(day1)
    # print(month2)


    if (year1 < 2023 and year2 < 2023) and (month2 <= month1) and (day1 < day2) :
    
     
        return True
    else:
        return False

date1 = '2017-08-02T00:00:00'
date2 = '2017-08-08T00:00:00'

print(timePeriod(date1, date2))

date1 = '2023-08-02T00:00:00'
date2 = '2017-08-08T00:00:00'
print(timePeriod(date1, date2))

date1 = '2079-08-02T00:00:00'
date2 = '2089-08-19T00:00:00'
print(timePeriod(date1, date2))

date1 = '2022-01-02T00:00:00'
date2 = '2022-01-12T00:00:00'
print(timePeriod(date1, date2))