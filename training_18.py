# fibonnaci with reccursion
'''
fibonnaci is a sequence of number that have a pattern like this: 1,1,2,3,5,8,13,..
'''

def fib(n):
  if n >= 3:
    # print(fib(n-1) + fib(n-2))
    return fib(n-1) + fib(n-2)
  else:
    # print(1)
    return 1

if __name__=="__main__":
  print(fib(5))