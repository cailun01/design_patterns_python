"""
ToHTMLDecorator装饰器改变了函数fib的输出
下一个: function_decorated_fib.py
"""

import time


class ProfilingDecorator(object):
  
  def __init__(self, f):
    print("Profiling decorator initiated")
    self.f = f

  def __call__(self, *args):
    print("ProfilingDecorator called")
    start_time = time.time()
    result = self.f(*args)
    end_time = time.time()
    print("[Time elapsed for n = {}] {}".format(n, end_time - start_time))
    return result


class ToHTMLDecorator(object):
  def __init__(self, f):
    print("HTML wrapper initiated")
    self.f = f
  
  def __call__(self, *args):
    print("ToHTMLDecorator called")
    return "<html><body>{}</body></html>".format(self.f(*args))


@ToHTMLDecorator
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


if __name__ == "__main__":
  n = 77
  print("Fibonacci number for n = {}: {}".format(n, fib(n)))