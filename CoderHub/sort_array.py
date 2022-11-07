

from typing import List
def sort_array(my_array: List[int], typeParam: str) -> List[int]:
    # write your code here ^_^
    if typeParam == "B":
        my_array.sort(reverse= True)
    elif typeParam == "S":
        my_array.sort()
    return my_array



my_array = [63,12,43,56,12]
typeParam = 'B'

print(sort_array(my_array, typeParam))