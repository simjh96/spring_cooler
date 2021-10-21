# def solution(gems):
#     answer = []
#
#     return answer
#
#
# gems = ["XYZ", "XYZ", "XYZ"]
#
#
# def trim(arr, counts: dict):
#     for _ in range(len(arr)):
#         if counts[arr[_][0]] > 1:
#             counts[arr[_][0]] -= 1
#
#         else:
#             arr = arr[_:]
#             break
#     print(f'from trim: {arr}')
#     return arr, counts
#
#
# full = set(gems)
# max_len = len(gems)
# answer = [0, len(gems) - 1]
# cand = []  # [(gem, idx), ..]
#
# curr_count = {gem: 0 for gem in gems}
#
# for _ in range(len(gems)):
#     # full set
#     if sum(map(lambda x: x[1]>0, curr_count.items())) == len(full):
#         print(cand)
#         cand, curr_count = trim(cand, curr_count)
#         print(f'after trim:{cand}')
#         if len(cand) < max_len:
#             answer = [cand[0][1] + 1, cand[-1][1] + 1]
#
#         curr_count[cand[0][0]] -= 1
#         cand.pop(0)
#     else:
#         print(cand)
#         cand.append((gems[_], _))
#         curr_count[gems[_]] += 1
#
#
# print(answer)
# # 왼쪽부터 오른쪽으로 end 확장
# # 모든 보석이 포함돼야 함으로 같은 보석이 나오지 않는 이상 start를 이동시킬 수 없음(한 그룹 안에 다른 그룹 절대 못만듬)
# # 모든 보석이 포함되는 순간 results_cand.append
# # 계속 이동하다 start와 대체 가능한 보석까지 포함시 start를 왼쪽으로 이동(반복)
# # 위 절차 반복
#
# # substring
# # forward topo

from collections import defaultdict
d = defaultdict(int)
d[1] = 1
d.pop(1)
print(d.keys())