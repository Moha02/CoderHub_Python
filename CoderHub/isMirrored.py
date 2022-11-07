from typing import List
import math
def isMirrored(num: int) -> bool:
    # write your code here ^_^
    num = str(num)
    reversed_num = num[::-1]
    if num == reversed_num:
        return True
    else:
        return False
    

    # num[0], num[-1] = num[-1], num[0]
    # return num

print(isMirrored(11))
print(isMirrored(16461))
print(isMirrored(112))
