from re import L
from typing import List
def most_frequent_element(arr: List[int]) -> int:
    # write your code here ^_^
    o = arr.count(2)
    return max(set(arr), key = arr.count)


arr = [13,2,1,2,10,2,1,1,2,2]
print(most_frequent_element(arr))