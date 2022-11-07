

from typing import List
def average(values: List[int]) -> float:
    # write your code here ^_^
    length = len(values)
    sum1 = 0
    for x in values:
        sum1 = sum1 + x
    avg = sum1 / length
    return avg

values = [2,4,9,23,435]
print(average(values))