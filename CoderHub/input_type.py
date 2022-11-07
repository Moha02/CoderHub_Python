

from curses.ascii import isalnum
from tokenize import Double
from typing import List
def input_type(value: str) -> str:
    # write your code here ^_^
    z = type(value)
    print(z)






value = 'hello'
print(input_type(value))

value = '21.21'
print(input_type(value))