from collections import deque 

from typing import List
from unittest import result
def postFix(expr: str) -> int:
    # write your code here ^_^
    Operators = set(['+', '-', '*', '/', '(', ')', '^']) 
    
    stack = [] # initialization of empty stack

    resultL = []

    stack = []
    operator = []
    expr = expr.split(" ")
    t = 0
    # print(expr)
    # traverse the given expression
    for x in range(len(expr)):
        if(expr[x].isdigit()==True): 
            stack.append(int(expr[x]))
        else:
            operator.append(expr[x])
    x = 0
    for x in range(0, 2):
        try:
            if operator[x] == "+":
                print(f"x :{stack[x]}. x+1 : {stack[x+1]}")
                result = stack[x] + stack[x+1]
                stack.pop()
                # stack.pop()
                resultL.insert(x, result)
            elif operator[x] == "-":
                print(f"x :{stack[x]}. x+1 : {stack[x+1]}")
                result = stack[x] - stack[x+1]
                # stack.pop()
                # stack.pop()
                resultL.insert(x, result)
            elif operator[x] == "/":
                print(f"x :{stack[x]}. x+1 : {stack[x+1]}")
                result = stack[x] / stack[x+1]
                # stack.pop()
                # stack.pop()
                resultL.insert(x, int(result))
            elif operator[x] == "*":
                print(f"x :{stack[x]}. x+1 : {stack[x+1]}")
                
                result = stack[x] * stack[x+1]
                # stack.pop()
                # stack.pop()
                resultL.insert(stack.index, int(result)) 
            x += 1
        except IndexError as e :
            pass
    # for x in range(2):
    #     try:
    #         if operator[x] == "+":
    #             result = stack[x] + stack[x+1]
    #             stack.pop(x)
    #             stack.pop(x)
    #             stack.insert(x, result)
    #         elif operator[x] == "-":
    #             result = stack[x] - stack[x+1]
    #             stack.pop(x)
    #             stack.pop(x)
    #             stack.insert(x, result)
    #         elif operator[x] == "/":
    #             result = stack[x] / stack[x+1]
    #             stack.pop(x)
    #             stack.pop(x)
    #             stack.insert(x, int(result))
    #         elif operator[x] == "*":
    #             result = stack[x] * stack[x+1]
    #             stack.pop(x)
    #             stack.pop(x)
    #             stack.insert(x, int(result))
    #     except IndexError as e:
    #         pass
    # print(stack)
    # print(operator)     
        
        





    # for ch in expr:
 
    #     # if the current is an operand, push it into the stack
    #     if ch.isdigit():
    #         stack.append(int(ch))

    #     elif ch == '+':
    #         operator.append(stack[0] + stack[1])
    #     elif ch == '-':
    #         operator.append(stack[0] + stack[1])
    #     elif ch == '*':
    #         operator.append(stack[0] + stack[1])
    #     elif ch == '/':
    #         operator.append(stack[0] + stack[1])
 
       
    return resultL
    

expr = '6 2 / 3 +'
print(postFix(expr))

expr = '10 4 - 3 / 2 *'
print(postFix(expr))
expr = '4 2 /'
print(postFix(expr))

expr = '10 1 + 11 /'
print(postFix(expr))