

from typing import List
def similarOrdered(word1: str, word2: str) -> str:
    # write your code here ^_^
    word1 = "".join(sorted(set(word1), key=word1.index))
    word2 = "".join(sorted(set(word2), key=word2.index))
    
    word1 = list(word1)
    word2 = list(word2)
    word1.sort()
    word2.sort()
    print(word1)
    print(word2)
    st = ""
    counter = 0

    while True:
        try:
            if word1[counter] == word2[counter]:
                st = st + word1[counter]
                if len(word1) > counter and len(word2) > counter:
                    counter += 1
                print(st)
            elif word1[counter] != word2[counter]:
                break
            elif len(st) == 0:
                print("No found")
        except IndexError as e:
            pass

        # return st
    #     else:

    # print(st)

    # for x  in word1:
    #     if word1.count(x) > 1 :
    #         word1 = list(word1).remove(x)
    #         print(word1)
    # for x  in word2:
    #     if word2.count(x) > 1 :
    #         list(word2).remove(x)
    #         print(word2)
    
    


    # word_1 = list(word1)
    
    # word_2 = list(word2)
    # word_1.sort()
    # word_2.sort()
    # word_1= set(word_1)
    # word_1= set(word_2)

    # len1 = len(word_1)
    # len2 = len(word_2)

    # st = ""

    # for x in range(len(word_1)):
    #     if word_1[x] == word_2[x]:
    #         st = st + word_1[x]
    #     elif word_1[x] == word_2[x]:
    #         st = ""
    # return st


    # if len1 < len2:
    #     size = len2
    # else:
    #     size = len1

    # for x in range(0, size):
    #     try:
    #         if word_1[x] == word_2[x]:
    #             sims = sims +  word_1[x]
    #         elif word_1[x] != word_2[x]:
    #             break
    #     except IndexError as e:
    #         pass
    

    # if len(sims) == 0:
    #     return "No matches found"
    # else:
    #     return sims

    
    
    

word1 = 'washing'
word2 = 'waiting'

print(similarOrdered(word1, word2))

word1 = 'me'
word2 = 'meet'
print(similarOrdered(word1, word2))
# word1 = 'Reem'
# word2 = 'Nouf'
# print(similarOrdered(word1, word2))
word1 = 'abcdefggghi'
word2 = 'abcdefghirr'
print(similarOrdered(word1, word2))