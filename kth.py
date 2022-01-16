n = int(input())
k = int(input())
total = n ** 2


# range 1 ~ n**2
def get_le(guess):
    le = 0
    for i in range(1, n + 1):
        le += min([guess // i, n])
    return le


left = 1
right = n ** 2
answer = None

while left <= right:
    mid = (right + left)//2
    le = get_le(mid)

    if le >= k:
        right = mid - 1
        answer = mid
    elif le < k:
        left = mid + 1
    # print(f'left:{left} mid:{mid}/ answer: {answer} right:{right} -> le: {le}')

print(answer)
