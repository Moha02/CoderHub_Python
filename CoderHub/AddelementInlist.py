

def cumlative(arr):
    sum = []
    index = 0
    d = 0
    for x in arr:
        
        if index == 0:
            sum.append(arr[index])
            index += 1
        else:
            
            a = sum[d] + arr[index]
            sum.insert(index, a)
            index += 1
            d += 1
            
    return sum

arr = [2,4,8]
arr1 = [0,0,0]
arr2 = [3,4,5]
arr3 = [-4,-3,-2]

print(cumlative(arr))
print(cumlative(arr1))
print(cumlative(arr2))     
print(cumlative(arr3))       
