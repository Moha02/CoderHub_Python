
from typing import List
def count_ones(num: int) -> int:
    # write your code here ^_^
    bi = bin(num)
    bi = str(bi)
    ones = 0
    for x in bi:
        if x == "1":
            ones += 1
    
    return ones
    # if num >= 1:
    #     count_ones(num // 2)
    # bin = (num % 2, end="")
    # print(bin)

print(count_ones(100))