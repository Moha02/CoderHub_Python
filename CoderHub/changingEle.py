

def changngElements(arr):
    marr = []

    for x in arr:
        
        if x % 2 == 0 :
            x += 1
            marr.append(x)
        else:
            x -= 1
            marr.append(x)
    return marr
numbers = [73,221,52,214]
print(changngElements(numbers))