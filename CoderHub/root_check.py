

def root_check(sqr: float, num: int) -> int:
    # write your code here ^_^
    ans = sqr **(1./2.)
    if num == ans:
        return num
    else:
        return 0

sqr = 49
num = 8
print(root_check(sqr, num))

sqr = 64
num = 8
print(root_check(sqr, num))