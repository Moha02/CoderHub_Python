from typing import List
def numbers_range(number: int) -> str:
    # write your code here ^_^
    newstr = ""
    number = number + 1
    for x in range(number):
        if x == 0:
            x = str(x)
            newstr = x
        elif x >= 1:
            x = str(x)
            newstr = newstr + " " + x
    return newstr


print(numbers_range(4))

print(numbers_range(8))

print(numbers_range(9))

print(numbers_range(0))

