# from curses.ascii import isupper
# from typing import List
# import re
# def cap_space(txt: str) -> str:
#     # write your code here ^_^
#     l = []
 
#     # Printing Initial string
#     print ("Initial String", txt)
 
#     res_pos = [i for i, e in enumerate(txt+'A') if e.isupper()]
#     res_list = [txt[res_pos[j]:res_pos[j + 1]]
#             for j in range(len(res_pos)-1)]
 
#     # Printing result
#     print("Resultant prefix", str(res_list))
 

    
#     return res_list

from typing import List
import re
def cap_space(txt: str) -> str:
    # write your code here ^_^
    l = re.sub( r"([A-Z])", r" \1", txt).split()
    new_sentence = ""

    for x in range(len(l)):
        l[x] = l[x].lower()
        new_sentence = new_sentence + " " + l[x]
    return new_sentence
    



txt1 = 'wePlayTennis'
txt2 = 'iLikeCats'
txt3 = 'computerScience'
txt4 = 'thankYou'
# print(txt[2:])
# print(txt[:2])

print(cap_space(txt1))
print(cap_space(txt2))
print(cap_space(txt3))
print(cap_space(txt4))