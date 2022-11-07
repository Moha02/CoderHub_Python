from typing import List
def unique(arr: List[int]) -> List[int]:
    # write your code here ^_^
    l = []
    for x in arr:
        z = arr.count(x)
        if z == 1:
            l.append(x)
    return l



    # count = 0
    # l = []
    # countl = []
    # for x in range(0, len(arr)):

    #     if x == 0:
    #         l.append(arr[x])
    #     elif x > 0:
    #         if arr[x] in l:
    #             pass
    #         elif arr[x] not in l:
    #             countl.append(arr[x])
    # return countl





arr = [1,1,1,2,1,1]
print(unique(arr))

arr = [3,-4,3,3,3]
print(unique(arr))

arr = [2,4,-2]
print(unique(arr))

arr = [2,3,2,6,2]
print(unique(arr))