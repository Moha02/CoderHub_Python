

from typing import List
def getBiggestShared(a: List[int], b: List[int]) -> int:
    # write your code here ^_^
    l = []
    for x in a:
        if x in b:
            l.append(x)
    z = max(l)
    return z

a = [1,2,4,5]
b = [3,4,7,11]
getBiggestShared(a, b)

a = [90,95]
b = [90,95]
getBiggestShared(a, b)

