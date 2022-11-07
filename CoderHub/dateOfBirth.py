

def ksumSubset(date):
    date = int(date[:4])

    if date > 2018:
        return False
    elif date < 1822:
        return False
    else:
        return True





dateString1 = '2099-08-02T00:00:00'
dateString2 = '2017-10-21T00:00:00'
dateString3 = '1111-08-29T00:00:00'
dateString4 = '3020-01-01T00:00:00'

print(ksumSubset(dateString1))
print(ksumSubset(dateString2))
print(ksumSubset(dateString3))
print(ksumSubset(dateString4))

# def kSumSubset(dateString: str) -> bool:
#     # write your code here ^_^
#     dateString = int(dateString)
    
#     if date > 2018:
#         return False
#     elif date < 1822:
#         return False
#     else:
#         return True