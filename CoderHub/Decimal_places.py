

from typing import List
def Decimal_places(num: str) -> int:
    # write your code here ^_^
    
    dot = num.find(".")
    dot += 1
    if dot > 0:
        newnum = num[dot:]
        newnum = len(newnum)
        return newnum
    else:
        return 0


    print(dot)
    print(newnum)   

num = '3.967'

print(Decimal_places(num))

num = '300'

print(Decimal_places(num))