

from curses.ascii import islower
from typing import List
def reverse_case(strParam: str) -> str:
    # write your code here ^_^
    s = ""
    for x in strParam:
        upper = x.isupper()
        
        if upper is True:
            x = x.lower()
            s = s + x   
        else:
            x = x.upper()
            s = s + x
            
    return s
strParam = 'TeSt'
print(reverse_case(strParam))
