from typing import List
def less_or_more_than_zero(number: int) -> str:
    # write your code here ^_^
    if number > 0:
        return 'Greater than zero'
    elif number < 0:
        return 'Greater than zero'
    elif number == 0:
        return 'Equal to zero'

print(less_or_more_than_zero(10))

print(less_or_more_than_zero(-3))

print(less_or_more_than_zero(0))