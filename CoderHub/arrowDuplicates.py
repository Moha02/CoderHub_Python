

from typing import List
def arrowDuplicates(word: str) -> str:
    # write your code here ^_^
    state = ""
    word = word.upper()
    for char in word: 
        counts=word.count(char)
        print(char,counts)
        if counts > 1:
            state = state + "<"
        else:
            state = state + ">"
    return state



 

# print(arrowDuplicates("Hi"))

print(arrowDuplicates("Bb"))
# print(arrowDuplicates("SAFCSP"))
print(arrowDuplicates("JAVA"))