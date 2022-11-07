

def calculate_sum(lst):
    s = 0
    for x in lst:
        if x == 7:
            return 0
        s = s + x
    return s
lst = [1,2,3,4]
print(calculate_sum(lst))

lst = [0,7,12,67]
print(calculate_sum(lst))

lst = [23,43,27,87,67]
print(calculate_sum(lst))

lst = [84,469]
print(calculate_sum(lst))