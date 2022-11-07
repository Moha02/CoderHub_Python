

from curses.ascii import isalpha


def isEmail(email: str) -> bool:
    # write your code here ^_^

    first = email.partition("@")
    second = email.partition(".")
#     print(first)
#     print(second)
# ####################################################
#     # a = email.find("@")
#     # b = email.find(".")
#     # firstSec = email[:a]
#     # secondSec = email[a+1:b]
#     # thirdSec = email[-2:]
#     # print(thirdSec)
#     # print(firstSec)
#     # print(secondSec)
#     # print(thirdSec)
    if email:
        if len(first[0]) >= 1:
            if email[0].isalpha():
                if first[1] == "@" and second[1] == ".":
                    if len(first[0]) > 0:
                        if len(second[2]) > 2:
                            return True
                
    return False
#####################################################3

    # if len(firstSec) < 1:
    #     return False
    # else:
    #     pass
    # if firstSec[1].isalpha()==True:
    #     pass
    # else:
    #     return False
    # if len(firstSec) >= 1:
    #     pass
    # else:
    #     return False
    # if email.__contains__("@") == True:
    #     pass
    # else:
    #     return False
    # if len(secondSec) >= 2:
    #     pass
    # else:
    #     return False 
    # if email.__contains__(".") == True:
    #     pass
    # else:
    #     return False
    # if len(thirdSec) >= 2:
    #     pass
    # else:
    #     return False
    # return True
        
email = 'example@e.com'
print(isEmail(email))
email = 'example@example.com'
print(isEmail(email))

email = 'exampleexample.c'
print(isEmail(email))
email = 'example@com'
print(isEmail(email))
email = '@example.com'
print(isEmail(email))