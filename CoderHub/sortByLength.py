

def sortByLength(txt):
    newstr = ""
    txt = txt.split(" ")

    txt.sort(key=len)
    z = 0
    for x in txt:
        if z == 0:
            newstr = x
            z += 1
        else:
            newstr = newstr + " " + x
    return newstr

    # d[count] = x


        
    
txt = 'Have a wonderful day'
txt1 = 'I see you'
txt2 = 'Get in the boat'
txt3 = 'Do you speak English'
print(sortByLength(txt))
print(sortByLength(txt1))
print(sortByLength(txt2))
print(sortByLength(txt3))