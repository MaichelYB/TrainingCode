# jumped frog
'''
assume that a frog want to cross the river. The river's width is 11 feet with one stone every one feet.
assume that a frog can jump each rock, or it can skip 1 rocks when it's jump.
'''

def jump(n):
  if n >= 2:
    return jump(n-1) + jump(n-2)
  else:
    return 1

if __name__=="__main__":
  print(jump(10))