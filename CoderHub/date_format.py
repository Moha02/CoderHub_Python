from datetime import datetime
def date_format(date: str) -> str:

    
    z = datetime.strptime(date, "%Y/%m/%d").strftime("%Y-%-m-%-d")
    # print(datetime.fromisoformat(z))
    # print(f" Z: {z}")
    y = datetime.strptime(date, "%Y/%m/%d").strftime("%-m/%-d/%Y")
    # print(f"Y: {y}")

    full_date = f"{date} | {z} | {y}"
    # print(type(full_date))
    
    return full_date
    
    #     elif x == 1:
    #         z = date[:4]
    #         d = date[5:]
    #         # date2 = date[-3:]+ "/" + date[:4]
    #         date3 = d + "/" + z
    #         # print(date3)
    #     elif x == 2:
    #         full_date = (f"{date} | {date0} | {date3}")
            
    # return full_date


date1 = '2020/1/1'
date2 = '2019/12/28'
date3 = '2010/10/30'
date4 = '2013/11/29'



print(date_format(date1))
x = '2020/1/1 | 2020-1-1 | 1/1/2020'
print(x)
print(date_format(date2))
x ="2019/12/28 | 2019-12-28 | 12/28/2019"
print(x)
print(date_format(date3))
x = '2010/10/30 | 2010-10-30 | 10/30/2010'
print(x)
print(date_format(date4))
x = '2013/11/29 | 2013-11-29 | 11/29/2013'
print(x)