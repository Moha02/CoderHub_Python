

from typing import List
def stringCheck(value: List[str]) -> bool:
    # write your code here ^_^
    index = 1
    for x in value:
        if x == value[index]:
            print("=")
            print(f" x  : {x},  index {value[index]}")
            
            return True
        elif x != value[index]:
            print("!")
            print(f" x  : {x},  index {value[index]}")
            
            return False

value = ['Code','Code','Code']
print(stringCheck(value))

value = ['Hi','By']
print(stringCheck(value))