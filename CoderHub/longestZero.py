


from typing import List
def longestZero(strParam: str) -> str:
    # write your code here ^_^

    strParam = strParam.split("1")
    # print(strParam)
    return max(strParam)
    # zeors = 0

    # newStr = ""
    # for x in range(0,len(strParam)-1):

    #     if strParam[x] == "0"  :
    #         # if strParam[x + 1] == "0":
    #         zeors += 1
    #         newStr = newStr + strParam[x]
        
    #     elif strParam[x] =="1":
    #         pass
    # if len(newStr) == 0:
    #     return " "
    # else:
    #     return newStr
    


strParam = '100010'
print(longestZero(strParam))
strParam = '110011'
print(longestZero(strParam))
strParam = '00001'
print(longestZero(strParam))
strParam = '111001111'
print(longestZero(strParam))
strParam = '111'
print(longestZero(strParam))