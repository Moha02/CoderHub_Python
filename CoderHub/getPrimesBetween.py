

def f(a, b):
    l = []
    for x in range(a,b+1):  
         
        if x > 1:  
            for i in range (2, x):  
                if (x % i) == 0:  
                    break  
            else:
                l.append(x)  
    return l

a = 1
b = 10
print(f(a,b))

a = 20
b = 50
print(f(a,b))

a = 90
b = 100
print(f(a,b))

a = 53
b = 67
print(f(a,b))