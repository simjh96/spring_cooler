n = 4 
m = 3

combs = [[1, 2, 3], [1, 3, 4], [1, 2, 4]]

odd = set([_ for _ in range(1,n+1)])
even = set()

answer = [False]


def boom(arr):
    return any(map(lambda x: all([(_ in arr) for _ in x]), combs))


def dfs(_odd, _even, i=0):
    print("================================")
    print(' '*i + f'_odd : {_odd}')
    print(' '*i + f'_even : {_even}')
    
    if i==(2*n-1):
        answer[0] = True
    else:
        if i % 2:
            if not boom(_odd):
                dfs(_odd, _even, i+1)

            else:
                print(' '*i + f'boom : boom!')
        else:
            if not boom(_even):
                for o in _odd:
                    print(' '*i + f"{_odd} --{o}--> {_even}")
                    _odd.remove(o)                
                    _even.add(o)
                    dfs(_odd, _even, i+1)
                    _odd.add(o)
                    _even.remove(o)
            else:
                print(' '*i + f'boom : boom!')


dfs(odd, even)
print(answer)


            

