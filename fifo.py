def solution(n, cores):
    left = 0
    right = 10**9

    # binary search 가 흝어보지 못하는 영역: f(left)~f(right) 밖
    if n <= get_in_p(cores, left):
        return n

    # 작은쪽 끝자락
    while left < right:
        mid = left + (right-left)//2
        if n <= get_in_p(cores, mid):
            right = mid
        else:
            left = mid + 1

    # 필요한만큼 곧 돌아오는거에서 뽑아 쓰자
    required = n - get_in_p(cores, mid)
    if required <= 0:
        mid -= 1
        required = n - get_in_p(cores, mid)

    # 가장 빨리 돌아오는 순/ stable
    rs = get_remains(cores, mid)
    return rs[required - 1][0] + 1


def get_in_p(cores, k):
    return sum(map(lambda x: k//x + 1, cores))


# 더 필요할 경우
def get_remains(cores, k):
    return sorted([(i, r) for i, r in enumerate(map(lambda x: x - k % x, cores))], key=lambda y: y[1])

