from typing import List
def match_arrays(array1: List[str], array2: List[str]) -> bool:
    # write your code here ^_^
    s = []
    index = 0
    for x in range(len(array1) ):
        # for z in array2:

        if array1[x] in array2:
            s.append(array1[x])
        else:
            break

        # if array2[x] in array1:
        #     s.append(array1[x])
    if len(s) == len(array1) and len(s) == len(array2):
        return True
    else:
        return False
    return s
    #         if x == z:
    #             s.append(z)
    #             index += 1
    #             # print(s)
    #         else:
    #             index += 1
    # if len(array1) == len(s):
    #     return True
    # else:
    #     return False
    

array1 = ['hello','there','word2']
array2 = ['hello','there','word2']
print(match_arrays(array1, array2))

array1 = ['hello','word2']
array2 = ['hello','there','word2']
print(match_arrays(array1, array2))

array1 = ['hello','there','word2']
array2 = ['hello','word2']
print(match_arrays(array1, array2))

array1 = ['hello','there','word2']
array2 = ['word2','there','hello']
print(match_arrays(array1, array2))