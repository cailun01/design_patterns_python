import time

"""
计算斐波那契数列，并统计计算时间：
  start_time = time.time()
  计算。。。
  end_time = time.time()

总时间 = end_time - start_time
"""
N = 77

start_time = time.time()

def fibIter(n):
  fibPrev = 1
  fib = 1
  for num in range(2, N):
    fibPrev, fib = fib, fib + fibPrev
    return fib

end_time = time.time()

print("[Time elapsed for N = {}] {}".format(N, end_time - start_time))
print("Fibonacci number for N = {}: {}".format(N, fibIter(N)))