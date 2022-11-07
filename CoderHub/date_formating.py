
import datetime
from typing import List
def date_formating(date: str) -> str:
    # write your code here ^_^
    

    z = datetime.datetime.strptime(date, "%Y-%m-%d")
    x = datetime.datetime.strftime(z, "%d-%m-%Y")

    return x

date = '1954-09-01'
print(date_formating(date))
date = '2020-01-01'
print(date_formating(date))
date = '2021-01-01'
print(date_formating(date))
date = '2000-12-07'
print(date_formating(date))