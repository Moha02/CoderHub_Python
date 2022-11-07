from typing import List
from string import punctuation
def removeSpecialCharacters(strParam: str) -> str:
    # write your code here ^_^
    # newstr = ''.join((ch if ch in 'ABCDEFGHIJKlnopqrstupxyz' else ' ') for ch in strParam)
    # return newstr
    # low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '-']
    # char = "][()\"#/@;$:<>}{\'`+=~|.!?,]"
    
    symbols2 = ["-", "_"]
    newstr = strParam
    
    for x in strParam: 
        if x.isalpha():
            pass
        elif x != "_" and x != "-" and x != " ":
            newstr = newstr.replace(x, "")
    
    return newstr

    


    # for x in strParam:    
    #     if x in low or x in upper:
    #         pass
    #     elif x not in low or x not in upper:
    #         newstr = newstr.replace(x, " ")
    # # print(type(newstr))
    
    

strParam = 'Hi How are you!' 
print(removeSpecialCharacters(strParam))

strParam = 'Are_u_coming?'
print(removeSpecialCharacters(strParam))

strParam = 'Nora Rahaf$'
print(removeSpecialCharacters(strParam))

strParam = 'Solve-the-challenge'
print(removeSpecialCharacters(strParam))
    # low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # newstr = strParam
    # check = True
    # for x in strParam:
    #     check = x.isalpha()    
    #     if check == True:
    #         pass
    #     elif check != True:
    #         newstr = newstr.replace(str(x), " ")
    # return newstr