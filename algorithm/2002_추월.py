# 앞의 리스트와 뒤 리스트를 비교
# 순서가 다르다? 흠...
# from sys import stdin; input = stdin.readline

# N = int(input())

# car_in = tuple(input().rstrip() for _ in range(N))
# car_out = tuple(input().rstrip() for _ in range(N)) 

from sys import stdin; input = stdin.readline

N = int(input())
car_in = [input().rstrip() for _ in range(N)]
check = {car: False for car in car_in}

idx = 0
cnt = 0
for _ in range(N):
    last = input().rstrip()
    
    while check[car_in[idx]]:
        idx += 1
    if last == car_in[idx]:
        idx += 1
    else:
        cnt += 1
    check[last] = True
print(cnt)