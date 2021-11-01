answer = ['AKARAKA']
def aka_pel(arr):
    if len(arr) <= 1:
        return 
    else:
        print(f'arr[:len(arr)//2]:{arr[:len(arr)//2]}')
        print(f'arr[len(arr)-len(arr)//2::][::-1]:{arr[len(arr)-len(arr)//2::][::-1]}')
        if arr[:len(arr)//2] == arr[len(arr)-len(arr)//2::][::-1]:
            aka_pel(arr[:len(arr)//2])
        else:
            answer[0] = 'IPSELENTI'


aka_pel('aakaaaakaa')
print(answer[0])