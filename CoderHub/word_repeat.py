from typing import List
def word_repeat(word: str, n: int) -> str:
    # write your code here ^_^
    newword = ""

    for x in range(0, n):
        if x == 0:
            newword = word
        if x >= 1:
            newword = newword + " " + word 
        
    # newwor = word + " "
    # newword =  word * n
    return newword
    

word = 'Hi'
n = 2
print(word_repeat(word, n))
