from typing import List
def delete_element_in_array(arr: List[int], index: int) -> List[int]:
    # write your code here ^_^
    re = arr[index]
    arr.remove(re)
    return arr
arr = [3,2,4,88]
index = 2
print(delete_element_in_array(arr, index))

arr = [3,-3,4,0]
index = 0
print(delete_element_in_array(arr, index))

arr = [2,4,5]
index = 1

print(delete_element_in_array(arr, index))

arr = [1,2,3]
index = 0
print(delete_element_in_array(arr, index))