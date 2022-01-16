# arr=[(0,3), (idx, priority), ...], k=(5, priority)
def _solution(arr: list, k: tuple, cnt: int = 0):
    m = max(arr, key=lambda x: x[1])[1]
    for i in range(len(arr)):
        if arr[i][1] == m:   # pop if max
            if arr[i] == k:
                return cnt
            else:
                return _solution(arr[i+1:] + arr[:i], k, cnt+1)
