"""
下一个：func_attrs.py
"""

import time

# 闭包，内部作用域对外部作用域的内容进行引用
def profiling_decorator(f):
  # wrapped_f函数可以使用传给profiling_decorator的参数：f
  def wrapped_f(n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print( "[Time elapsed for n = {}] {}".format(n, end_time - start_time))
    return result
  return wrapped_f


# fib = profiling_decorator(fib)
@profiling_decorator
def fib(n):
  print("Inside fib")
  if n < 2:
    return
  
  fibPrev = 1
  fib = 1
  for num in range(2, n):
    fibPrev, fib = fib, fib + fibPrev
  return fib


if __name__ == "__main__":
  n = 77
  print("Fibonacci number for n = {}: {}".format(n, fib(n)))