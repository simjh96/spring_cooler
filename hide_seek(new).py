import time

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
def hide_seek(n, k):
    steps = 0
    visited = {n}
    positions = {n}
    limit = 10**5

    while True:
        # print(f'steps : {steps}')
        # print(f'max position : {max(positions)}')
        positions_ = set()
        if k in visited:
            break
        for vertex in positions:
            if (vertex+1 not in visited) and (limit >= vertex + 1 >= 0):
                positions_.add(vertex + 1)
                visited.add(vertex + 1)
            if (vertex-1 not in visited) and (limit >= vertex - 1 >= 0):
                positions_.add(vertex - 1)
                visited.add(vertex - 1)
            if (vertex*2 not in visited) and (limit >= 2*vertex >= 0):
                positions_.add(2*vertex)
                visited.add(2*vertex)
        steps += 1
        positions = positions_

    return steps


if __name__ == "__main__":
    n, k = map(int, input().split())

    print(hide_seek(n, k))

