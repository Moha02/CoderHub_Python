

from typing import List
def factorial(number: int) -> int:
    # write your code here ^_^
    s = []
    sumnum = 1
    for x in range(1, number + 1):
        s.append(x)
    for z in s:
        sumnum = sumnum * z
    return sumnum
        
        
print(factorial(number=10))