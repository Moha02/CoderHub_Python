def addStrNums(num1: str, num2: str) -> str:
    # write your code here ^_^
    try:
        n = int(num1)
        m = int(num2)
    except ValueError as e:
        x = -1
        x = str(x)
        return x
    result = n + m
    result = str(result)
    # print(type(result))
    return result
print(addStrNums("4", "6"))
print(addStrNums("5", "hi"))
print(addStrNums("1", "0"))
print(addStrNums("2", "1"))