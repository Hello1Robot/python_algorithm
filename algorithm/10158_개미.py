# 시간초과. IM이었으면 통과했다...

#가로길이 N, 세로길이 M
M,N = map(int,input().split())

# 이거 필드 만들필요도 없음 사실. 범위 바꾸기임
# 가로가 6, 세로가 4라면 사실 +1만큼 만들어줘야 함
gmx, gmy = map(int,input().split())
max_cnt = int(input())
cnt = 0
x_move = 1
y_move = 1
while cnt < max_cnt:
    if gmx + x_move > M or gmx + x_move < 0:
        x_move *= -1
    if gmy + y_move > N or gmy + y_move < 0:
        y_move *= -1
    gmx = gmx + x_move
    gmy = gmy + y_move
    cnt += 1

print(gmx, gmy)