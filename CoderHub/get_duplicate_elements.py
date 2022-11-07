

from typing import List
def get_duplicate_elements(arr: List[int]) -> List[int]:
    # write your code here ^_^
    unique = []
    dup = []
 
    for i in arr:
        if i not in unique:
            unique.append(i)
        elif i not in dup:
            dup.append(i)
    return dup


arr = [2,3,2,3]
print(get_duplicate_elements(arr))

arr = [10,5,9,5]
print(get_duplicate_elements(arr))
arr = [6,3,12,12]
print(get_duplicate_elements(arr))
arr = [3,-9,-9,-4]
print(get_duplicate_elements(arr))