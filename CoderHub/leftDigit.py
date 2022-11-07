from typing import List
def left_digit(strParam: str) -> int:
    # write your code here ^_^

    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in strParam)
    listOfNumbers = [] 
    try:
        for i in newstr.split():
            listOfNumbers.append(int(i[0]))

    except ValueError as e:
        pass
    return listOfNumbers[0:]

strParam = 'Welcome2back'
print(left_digit(strParam))

strParam = 'nora30@gmail.com'
print(left_digit(strParam))

strParam = '9753'
print(left_digit(strParam))

strParam = '5'
print(left_digit(strParam))

def left_digit(strParam: str) -> int:
    # write your code here ^_^

    newstr = ''.join((ch if ch in '0123456789' else ' ') for ch in strParam)
    listOfNumbers = [] 
    try:
        for i in newstr.split():
            listOfNumbers.append(int(i[0]))

    except ValueError as e:
        pass
    return listOfNumbers[0]