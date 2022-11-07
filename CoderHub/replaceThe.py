
from typing import List
def replaceThe(txt: str) -> str:
    # write your code here ^_^
    irr = ['a', 'e', 'i', 'o' ,'u']
    index = txt.find("the")
    index += 4
    if txt[index] not in irr:
        txt = txt.replace("the", "a")
    elif txt[index] in irr:
        txt = txt.replace("the", "an")

    return txt

txt = 'Here is the plan'
print(replaceThe(txt))

txt = 'I ate the apple'
print(replaceThe(txt))
txt = 'I go to the mall'
print(replaceThe(txt))
txt = 'I want the orange'
print(replaceThe(txt))