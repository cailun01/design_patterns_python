import time

"""
想要统计某个函数计算的时间，只需要把该函数传入profile_me
计算数列的函数fib传入统计时间的函数profile_me
不足：
you must pre-define the parameters you want applied to
the timed function(这种方法确实有一些限制，因为您必须预先定义要应用于定时函数的参数。)

下一个：base_profiled_fib.py
"""

def fib(n):
  if n < 2:
    return

  fibPrev = 1
  fib = 1
  for num in range(2, n):
    fibPrev, fib = fib, fib + fibPrev
  return fib

def profile_me(f, n):
  start_time = time.time()
  result = f(n)
  end_time = time.time()
  print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))
  return result
  
if __name__ == "__main__":
  n = 77
  print("Fibonacci number for n = {}: {}".format(n, profile_me(fib, n)))