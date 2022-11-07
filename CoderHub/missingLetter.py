
from typing import List
def missingLetter(txt: str) -> str:
    # write your code here ^_^
    alpha ='abcdefghijklmnopqrstuvwxyz'

    indexz = 0
    indexx = 0
    for z in txt:
        indexz += 1

        for x in alpha:
            indexx += 1
        

            if x == z:
                print(f"X : {x}, Z: {z}")
                print(f"indexz: {indexz}, indexx: {indexx}")



txt = 'ghijk'
missingLetter(txt)
