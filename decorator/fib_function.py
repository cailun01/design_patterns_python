import time

"""
把time放在fib函数内。但是这个程序只能统计fib函数计算的时间，如果希望统计其他函数的时间呢？
Python中的函数是一等公民，可以作为参数

下一个：fib_func_profile_me.py
"""

def fib(n):
  start_time = time.time()
  if n < 2:
    return
  fibPrev = 1
  fib = 1
  for num in range(2, n):
    fibPrev, fib = fib, fib + fibPrev
  end_time = time.time()
  print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))
  return fib
  
if __name__ == "__main__":
  n = 77
  print("Fibonacci number for n = {}: {}".format(n, fib(n)))