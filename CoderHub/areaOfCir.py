
import math
def area(r):

    
    cir = math.pi * r ** 2 
    return cir



def find_circle_area(radius: float) -> float:
    # write your code here ^_^
    pi = 3.14
    area = pi * (radius ** 2) 
    return area

print(find_circle_area(5.4))
print(find_circle_area(7))
print(find_circle_area(1))
print(find_circle_area(10.2))