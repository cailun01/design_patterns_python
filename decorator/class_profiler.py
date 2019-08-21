"""
如果我们想装饰类的多个成员函数，最直接的办法，是把装饰器放在每个函数前：
class DoMathStuff(object):
  @profiling_decorator
  def fib(self):
    ...
  
  @profiling_decorator
  def factorial(self):
    ...
但是上面的做法违反了DRY原则(Don’t Repeat Yourself)。
"""

import time
from functools import wraps


def profiling_wrapper(f):
  @wraps(f)
  def wrap_f(*args, **kwargs):
    start_time = time.time()
    result = f(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("[Time elapsed for n = {}] {}".format(n, elapsed_time))
    return result
  return wrap_f


def profile_all_class_methods(Cls):
  class ProfiledClass(object):
    def __init__(self, *args, **kwargs):
      self.inst = Cls(*args, **kwargs)
    
    def __getattribute__(self, s):
      try:
        x = super(ProfiledClass, self).__getattribute__(s)
      except AttributeError:
        pass
      else:
        x = self.inst.__getattribute__(s)
        if type(x) == type(self.__init__):
          return profiling_wrapper(x) # profiling_wrapper是装饰器
        else:
          return x
  return ProfiledClass

"""
@profile_all_class_methods
class DoMathStuff(object):
  def fib(self):
    ...

  @profiling_decorator
  def factorial(self):
    ...
"""