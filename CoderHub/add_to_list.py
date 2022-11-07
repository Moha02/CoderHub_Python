
def add_five(arr):
    index = 0
    if len(arr) == 0:
        return arr
    else:
        for x in arr:
            arr[index] = arr[index] + "5"
            index += 1
    return arr

arr = ['code','c']
print(add_five(arr))