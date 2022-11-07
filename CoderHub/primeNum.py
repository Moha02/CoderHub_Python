
from array import array


numbers = [2,5,8,12,25]
def prime(array):
    l = []
    for number in array:  
        if number > 1:  
            for i in range (2, number):  
                if (number % i) == 0:  
                    break  
            else:
                l.append(number) 
    return l

print(prime(numbers))