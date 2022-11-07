

from typing import List
def bin_to_oct(b: str) -> int:
    # write your code here ^_^
    
    # if not all(char in "01" for char in b):
    #     raise ValueError("Non-binary value was passed to the function")
    # if not b:
    #     raise ValueError("Empty string was passed to the function")
    oct = ""
    while len(b) % 3 != 0:
        b = "0" + b
    bin_string_in_3_list = [
        b[index : index + 3]
        for index in range(len(b))
        if index % 3 == 0
    ]
    for bin_group in bin_string_in_3_list:
        oct_val = 0
        for index, val in enumerate(bin_group):
            oct_val += int(2 ** (2 - index) * int(val))
        oct += str(oct_val)
    
    return oct


    # print(c1)
    # return 

b = '101010101010'
print(bin_to_oct(b))

b = '1000000000'
print(bin_to_oct(b))
b = '10101111000'
print(bin_to_oct(b))
b = '1'
print(bin_to_oct(b))