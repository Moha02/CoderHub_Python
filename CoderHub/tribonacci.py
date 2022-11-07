# def fib(num):
#   """return the number at index num in the fibonacci sequence"""
#   if num <= 2:
#     return 1
#   return fib(num - 1) + fib(num - 2)
#     # print(fib(6))  # 8
# print(fib(9))

from inspect import signature


def tribonacci( n):
   signature = [1,1,1]
   # if n == 2:
   #    return [1 , 1]
   # elif n == 1:
   #    return [0, 1]
   # elif n == 0:
   #    return [0]
   if n:
      result = signature.copy()
      if n<3:
         return result[0:n]
      for x in range(2,n-1):
         el = result[x-2]+result[x-1]+result[x]
         result.append(el)
      return result
   return []

num = 0
signature = [1,1, 1]

print(tribonacci(num))

num = 5

print(tribonacci(num))
num = 6

print(tribonacci(num))

num = 9


print(tribonacci(num))