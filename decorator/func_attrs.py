"""
function_decorated_fib.py中使用的wrapper函数会改变函数的
__name__ 和 __doc__属性。functools的wraps禁止wrapper函数改变被装饰函数的__name__ 和 __doc__。

如果我们想设置时间的单位(s, ms等)，需要使用带参数的装饰器。
"""
from functools import wraps
import time

# profiling_decorator_with_unit是带参数的装饰器。
def profiling_decorator_with_unit(unit="seconds"):
  def profiling_decorator(f):
    @wraps(f) # 禁止wrapper函数改变被装饰函数的__name__ 和 __doc__
    def wrap_f(n):
      start_time = time.time()
      result = f(n)
      end_time = time.time()
      if unit == "seconds":
        elapsed_time = (end_time - start_time) / 1000
      else:
        elapsed_time = (end_time - start_time)
      print( "[Time elapsed for n = {}] {}".format(n, elapsed_time))
      return result
    return wrap_f
  return profiling_decorator


@profiling_decorator_with_unit("seconds")
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