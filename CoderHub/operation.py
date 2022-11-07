

def operation(num1: int, num2: int):
    if (num1 + num2 == 24):
        return "added"
    elif (num1 * num2 == 24):
        return "multiplied"
    elif (num1 / num2 == 24):
        return "divided"
    elif (num1 - num2 == 24):
        return "subtracted"
    else:
        return "None"

num1 = 6
num2 = 7

print(operation(num1, num2))

num1 = 20
num2 = 4
print(operation(num1, num2))
num1 = 3
num2 = 8
print(operation(num1, num2))
num1 = 24
num2 = 1
print(operation(num1, num2))