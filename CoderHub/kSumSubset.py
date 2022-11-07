

from typing import List
def kSumSubset(numArray: List[int], k: int) -> bool:
    # write your code here ^_^

    hashmap = {}
    leng = len(numArray)
 
    for i in range(0, leng):
        temp = k-numArray[i]
        if (temp in hashmap):
            return True
        hashmap[numArray[i]] = i
    return False




    # length = len(numArray)
    # for i in range(0, length - 1):
    #     for j in range(i + 1, length):
    #         if numArray[i] + numArray[j] == k:
    #             return True
    # return False


   # /////////////////////
    # index = 1
    # for x in numArray:
    #     print("///////////////////")

    #     for z in numArray:
    #         if x == z:
    #             continue
    #         print("--------------------------")
    #         print(f"x: {x}  ")
    #         print(f"numArray[index]: {z}  ")
    #         sum = x + z
    #         print(f"Sum: {sum}  ")
    #         index += 1
    #         if sum == k:
    #             print("Result =========================================")
    #             return True
    # print("Result =========================================")
    # return False


numArray = [7,3,2,5,8]
k = 14
print(kSumSubset(numArray, k))

numArray = [2,4,6,8]
k = 11
print(kSumSubset(numArray, k))
numArray = [7,5,3,1]
k = 4
print(kSumSubset(numArray, k))

numArray = [14,8,12,9]
k = 21
print(kSumSubset(numArray, k))