from typing import List
def array_root(arr: List[float]) -> List[float]:
    # write your code here ^_^
    l = []
    for x in arr:
        s = x ** (1/2)
        l.append(s)
    return l

arr = [4,81,49]
print(array_root(arr))