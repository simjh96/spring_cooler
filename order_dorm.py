names, homes, grades, result = ["azad","andy","louis","will","edward"], [[3,4],[-1,5],[-4,4],[3,4],[-5,0]], [4.19, 3.77, 4.41, 3.65, 3.58], [2,3,1,5,4]
grades = list(map(lambda x: int(x*100), grades))
print(list())
total = list(zip(names,homes,grades))
total.sort(key=lambda x: x[0])
total.sort(key=lambda x: x[1][0]**2 + x[1][1]**2, reverse=True)
total.sort(key=lambda x: x[2]//100, reverse=True)

final = dict()
f_list = list(map(lambda x: x[0],total))
for i in range(1, len(names)+1):
    final[f_list[i-1]] = i

print([final[n] for n in names])

