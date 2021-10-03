import sys
import time
import random

def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time


@timeit
def nge(n, a):
    result = [-1] * n
    stack = []
    idx_stack = []

    for i in range(n - 1):
        stack.append(a[i])
        idx_stack.append(i)
        while stack and stack[-1] < a[i + 1]:
            stack.pop()
            result[idx_stack.pop()] = a[i + 1]
    return result


if __name__ == "__main__":
    # n = int(sys.stdin.readline())
    # a = list(map(int, sys.stdin.readline().split()))

    n = 10 ** 6
    # a = list(range(10 ** 6))[::-1]
    a = random.choices(range(10 ** 6), k=10 ** 6)

    nge(n, a)





