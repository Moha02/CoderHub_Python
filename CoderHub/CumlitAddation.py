

def cam(array):
    arr = []
    sum = 0
    length = len(array)

    for x in array:
        sum = sum + x
    arr.append(sum)
    arr.append(length)
    return arr


elements_array = [5,1,2,4,9,10,200]
print(cam(elements_array))


def cumulative_addition(elements_array):
    # write your code here ^_^
    arr = []
    sum1 = 0
    length = len(elements_array)

    for x in elements_array:
        sum1 = sum1 + x
    arr.append(sum1)
    arr.append(length)
    return arr