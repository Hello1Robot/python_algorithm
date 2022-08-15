# 인덱스값과 밸류가 둘 다 필요한 문제
# DOWN일 경우 - 현재 인덱스보다 UP된 위치에 있어야 함
# UP일 경우에는 그 반대
# same의 경우, 그대로여야 함

N = int(input())
up_list = []
down_list = []
same_list = []
for i in range(N):
    a = input()
    b = input()
    if b == 'UP':
        up_list.append((i,a))
    elif b == 'DOWN':
        down_list.append((i,a))
    else:
        same_list.append((i,a))

down_list.sort()
up_list.sort()
same_list.sort()
res_list = []
for idx, val in down_list:
    res_list.append(val)
for idx, val in up_list:
    res_list.append(val)

for idx, val in same_list:
    down_list.insert(idx, val)

for dn in res_list:
    print(dn)
