import sys
import random

# sys.setrecursionlimit(10 ** 7)


# stones, k = [4, 2, 2, 1, 4], 1


def action(my_stones, i):
    # [stones, continuable]
    continuable = True
    _my_stones = []
    for _ in range(len(my_stones)):
        if _ == i:
            _stone = my_stones[_] + 1
            _my_stones.append(_stone)

        else:
            _stone = my_stones[_] - 1
            _my_stones.append(_stone)
            if _stone < 0:
                continuable = False
                break
    return [_my_stones, continuable]


def dfs(my_stones, history='', debug=0):
    if (len(my_stones) - sum(list(map(lambda x: x == 0, my_stones))) == 1) and (sum(my_stones) == k):
        answer.append(history)
    else:
        for i in range(len(my_stones)):
            _my_stones, continuable = action(my_stones, i)
            if continuable:
                print("===========")
                print(' '*debug + str(_my_stones))
                dfs(_my_stones, history + str(i), debug+1)


for _ in range(10):
    print("===============================")
    # try:
    stones, k = [random.randint(1, 30), random.randint(1, 30), random.randint(1, 30), random.randint(1, 30),
                 random.randint(1, 30)], random.randint(1, 30)
    answer = []
    print(f'stones: {stones}, k: {k}')
    dfs(stones)
    if answer:
        answer.sort(reverse=True)
        answer.sort(key=len)
        print(answer[0])
    else:
        print("-1")
    print(f'answer : {answer}')
    # except:
    #     print(stones)
    #     print(k)
    #     print(answer)



#
#
# 테스트 재설정
# 20214Q_SoftwareEngineer_코딩테스트_A for 심재훈
# Python3 레퍼런스
# 컴파일 옵션
# 1
# 2
# 3
# 4
# 5
# 2. 프로그래밍
# 종료까지
# 00:04:29
# 프로그래밍
# 다시 풀 문제
# 문제 설명
# 돌무더기 게임은 여러 돌무더기에서 돌을 하나씩 추가하거나 제거하여, 하나의 돌무더기만 남기는 게임입니다. 게임에서 승리하기 위해서는 마지막에 남은 하나의 돌무더기의 돌 수가 정확히 k개가 되어야 합니다.
#
# 처음 주어지는 돌무더기들은 각각 1개 이상의 돌을 갖고 있습니다. 당신은 한 돌무더기를 골라 다음과 같은 행동을 할 수 있습니다.
#
# 선택한 돌무더기에 돌을 1개 추가합니다. 동시에, 선택되지 않은 나머지 돌무더기에서 각각 1개씩 돌을 제거합니다.
# 돌을 제거해야 할 나머지 돌무더기 중에서 제거할 돌이 없는 경우(=돌 수가 0인 경우), 위 행동은 실행할 수 없습니다.
# 예를 들어 3개의 돌무더기에 돌이 각각 [1, 3, 2]개 있고 k가 3인 경우, 게임에서 승리하는 가장 빠른 방법은 아래와 같이 2가지가 있습니다.
#
# 첫 번째 - 세 번째 - 세 번째 돌무더기를 차례대로 선택합니다. 각 선택 시에 돌무더기의 돌 수는 [2, 2, 1] - [1, 1, 2] - [0, 0, 3]과 같이 변합니다.
# 세 번째 - 첫 번째 - 세 번째 돌무더기를 차례대로 선택합니다. 각 선택 시에 돌무더기의 돌 수는 [0, 2, 3] - [1, 1, 2] - [0, 0, 3]과 같이 변합니다.
# 선택하는 돌무더기의 인덱스를 순서대로 나열하여 문자열로 변환하면 1번 방법은 "022", 2번 방법은 "202"입니다. 이를 사전 순으로 정렬했을 때, 가장 뒤에 오는 방법은 "202"입니다.
#
# 각 돌무더기의 돌 수를 나타내는 정수 배열 stones, 남겨야 하는 한 돌무더기의 돌 수를 나타내는 정수 k가 매개변수로 주어집니다. 게임에서 승리하기 위한 가장 빠른 방법 중에서, 선택하는 돌무더기의 인덱스를 문자열로 변환했을 때 사전 순으로 가장 뒤에 오는 방법을 return 하도록 solution 함수를 완성해주세요. 만약 어떤 방법으로도 목표를 달성할 수 없다면 "-1"을 return 해주세요.
#
# 제한사항
# 2 ≤ stones의 길이 ≤ 8
# 1 ≤ stones의 원소 ≤ 12
# 1 ≤ k ≤ 24
# 돌 수가 0인 돌무더기도 선택할 수 있는 돌무더기입니다.
# 입출력 예
# stones	k	result
# [1, 3, 2]	3	"202"
# [4, 2, 2, 1, 4]	1	"3213"
# [5, 7, 2, 4, 9]	20	"-1"
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
#
# 입출력 예 #2
#
# 네 번째 - 세 번째 - 두 번째 - 네 번째 순으로 돌무더기를 선택하면 아래 표와 같이 돌 수가 변합니다.
#
# 선택한 돌무더기의 인덱스	stones
# -	[4, 2, 2, 1, 4]
# 3	[3, 1, 1, 2, 3]
# 2	[2, 0, 2, 1, 2]
# 1	[1, 1, 1, 0, 1]
# 3	[0, 0, 0, 1, 0]
# 따라서 "3213"을 return 합니다.
#
# 입출력 예 #3
#
# 어떤 방법으로도 마지막에 남길 한 돌무더기를 20으로 만들 수 없습니다. 따라서 "-1"을 return 합니다.
#
# 26분 전 저장됨
# 2321221920161718141512131011789563412
# import sys
# sys.setrecursionlimit(10**7)
# # 테스트 1, 2에서 inf recursion..
#
# def solution(stones, k):
#     def action(my_stones, i):
#         # [stones, continuable]
#         continuable = True
#         _my_stones = []
#         for _ in range(len(my_stones)):
#
# 실행 결과
# 같은 코드로 채점한 결과가 있습니다.
# 정확성 테스트
# 테스트 1 〉 실패 (시간 초과)
# 테스트 2 〉 실패 (시간 초과)
# 테스트 3 〉 통과 (0.28ms, 10.3MB)
# 테스트 4 〉 실패 (시간 초과)
# 테스트 5 〉 통과 (9.29ms, 10.2MB)
# 테스트 6 〉 실패 (시간 초과)
# 테스트 7 〉 실패 (시간 초과)
# 테스트 8 〉 실패 (시간 초과)
# 테스트 9 〉 통과 (6070.37ms, 12.8MB)
# 테스트 10 〉 실패 (시간 초과)
# 테스트 11 〉 실패 (시간 초과)
# 테스트 12 〉 실패 (시간 초과)
# 테스트 13 〉 통과 (4599.75ms, 17.9MB)
# 테스트 14 〉 통과 (51.57ms, 10.3MB)
# 테스트 15 〉 실패 (시간 초과)
# 테스트 16 〉 통과 (1186.87ms, 10.3MB)
# 테스트 17 〉 통과 (4295.33ms, 10.8MB)
# 테스트 18 〉 실패 (시간 초과)
# 테스트 19 〉 통과 (139.45ms, 10.3MB)
# 테스트 20 〉 통과 (7442.54ms, 10.7MB)
# 테스트 21 〉 통과 (116.83ms, 10.3MB)
# 채점 완료
#
#
#
#
#
# 시험이 5분 뒤에 종료됩니다.
# 시간 만료로 시험이 종료될 경우 저장된 답안 중 가장 높은 점수의 답안이 제출됩니다.