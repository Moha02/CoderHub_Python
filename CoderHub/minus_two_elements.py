from typing import List

def sub_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    # write your code here ^_^
    result = []
    for x in range(len(arr1)):
        a = arr2[x] - arr1[x] 
        result.insert(x, a)
    return result

# arr1 = [2,4,88]
# arr2 = [4,2,88]

# arr1 = [-3,4,0]
# arr2 = [93,22,7]

arr1 = [7,8,2]
arr2 = [4,5,1]

arr1 = [19,29]
arr2 = [10,20]

print(sub_arrays(arr1, arr2))