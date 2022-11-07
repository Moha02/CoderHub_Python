

from typing import List
def sum_even(arr: List[int]) -> int:
    # write your code here ^_^
    su1 = 0
    for x in arr:
        if x % 2 == 0:
            su1 = su1 + x
    return su1

arr = [11,0,5,22]
print(sum_even(arr))

arr = [16,3,9,2]
print(sum_even(arr))

arr = [12,65,42]
print(sum_even(arr))

arr = [1,3,7]
print(sum_even(arr))