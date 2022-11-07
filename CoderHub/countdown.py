

from typing import List
def countdown(num: int) -> List[int]:
    # write your code here ^_^
    num += 1
    q = 8
    l = []
    for x in range(0,num, q):
        if q == 2:
            print(num - 3)
            q +=1
            
        else:
            q += 2
            
        
            print(x)

countdown(103)