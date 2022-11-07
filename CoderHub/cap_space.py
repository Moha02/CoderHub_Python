from typing import List
import re
def cap_space(txt: str) -> str:
    # write your code here ^_^
    l = re.sub( r"([A-Z])", r" \1", txt).split()
    new_sentence = ""

    for x in range(len(l)):
        l[x] = l[x].lower()
        new_sentence = new_sentence + " " + l[x]
    return new_sentence[1:]

txt = 'wePlayTennis'
cap_space(txt)