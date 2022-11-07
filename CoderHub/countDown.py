

from typing import List
def countDown(number: int) -> str:
    # write your code here ^_^
    l = []
    for x in range(number, 1, -3):
        if x == number:
            pass
        elif x % 2 == 0:
            l.append(x)
        # elif x <= 3:
        #     re
    if len(l) == 0:
        return [0]
    l.reverse()
    return l


print(countDown(10))
print(countDown(23))
print(countDown(103))
print(countDown(15))
print(countDown(3))
