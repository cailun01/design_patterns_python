"""
The classic implementation of the decorator pattern uses the fact that the way Python
implements regular procedural functions these functions can be seen as classes with
some kind of execution method.

下一个：stacked_fib.py
"""

import time

class ProfilingDecorator(object):
  def __init__(self, f):
    print("Profiling decorator initiated")
    # 被装饰函数作为类的成员
    self.f = f

  def __call__(self, *args): # *args把传入的参数打包(packing)
    print("__call__")
    start_time = time.time()
    result = self.f(*args) # 解包(unpacking)arg
    end_time = time.time()
    print("[Time elapsed for n = {}] {}".format(n, end_time - start_time)) 
    return result


# 相当于 fib = ProfilingDecorator(fib)
@ProfilingDecorator 
def fib(n):
  print("Inside fib")
  if n < 2:
    return
  
  fibPrev = 1
  fib = 1
  for num in range(2, n):
    fibPrev, fib = fib, fib + fibPrev
  return fib

@ProfilingDecorator 
def fib2(n):
  print("Inside fib2")
  if n < 2:
    return
  
  fibPrev = 1
  fib = 1
  for num in range(2, n):
    fibPrev, fib = fib, fib + fibPrev
  return fib

# 先初始化ProfilingDecorator的构造函数，再调用类的成员函数__call__，最后调用fib。
# 然后打印 `[Time elapsed for n = ...`

if __name__ == "__main__":
  n = 77
  print("Fibonacci number for n = {}: {}, {}".format(n, fib(n), fib2(n-50)))