

# def math_exper(st):
#     signs = ["+", "-", "/", "*"]

#     for x in range(0, len(st)):
#         if x == 0 or x == 2:
#             try:
#                 num = int(st[x])
#             except ValueError as e:
#                 return False
#         elif x == 1:
#             if st[x] in signs:
#                 return True
#             else:
#                 return False
#     return True

             

def math_expr(expr: str) -> bool:
    # write your code here ^_^
    signs = ["+", "-", "/", "*"]

    for x in range(0, len(expr)):
        if x == 0 or x == 2:
            try:
                num = int(expr[x])
            except ValueError as e:
                return False
        elif x == 1:
            if expr[x] in signs:
                return True
            else:
                return False
    return True

# math_exper("8-6")

test = "6/1"
print(math_expr(test))