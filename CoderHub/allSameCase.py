from typing import List
def allSameCase(word: str) -> bool:
    # write your code here ^_^
    wordL = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    wordS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l = 0
    s = 0
    leng =len(word)
    for x in word:
        if x in wordL:
            l += 1
            print("L")
        elif x in wordS:
            print("S")
            s += 1
    if l == leng or s == leng:
        return True
    if s != leng or l != leng:
        return False

word = 'Hello'
print(allSameCase(word))
word = 'hello'
print(allSameCase(word))
word = 'HI'
print(allSameCase(word))
word = 'a'
print(allSameCase(word))

