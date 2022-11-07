
from math import ceil
from typing import List
def middle_char(word: str) -> str:
    # write your code here ^_^
    return word[(len(word)-1)//2:(len(word)+2)//2]
    # l = len(word)
    # leng = l / 2
    # s = ""
    # leng = ceil(leng)
    # if leng <= 1:
    #     s = word
    #     return s
    # elif leng % 2 == 0:
    #     m = leng - 1
    #     x = leng + 1
    #     s = (word[m:x])
    #     return s
    # elif leng % 2 != 0:
    #     leng -= 1
    #     s = (word[leng])
    #     return s

    

word = 'test'
print(middle_char(word))

word = 'z'
print(middle_char(word))

word = 'salem'
print(middle_char(word))

word = 'like'
print(middle_char(word))