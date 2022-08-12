dx = [0,1,0,-1]
dy = [1,0,-1,0]
res = 0
N, M = map(int, input().split())
field = [([0]*M) for _ in range(N)]
cnt = 1 # 값 + 종료포인트
idx = 0 # 방향값 설정하는 인덱스
field[0][0] = 1 # 첫번째 필드 미리 설정
que = []
x = 0 # 기본 x 값 설정
y = 0 # 기본 y 값 설정
while cnt < N*M: # 
    nx = x + dx[(idx%4)] # 다음으로 이동할 x값
    ny = y + dy[(idx%4)] # 다음으로 이동할 y값
    if nx < 0 or nx >= N or ny < 0 or ny >= M: # 범위를 벗어난 값일 때 방향 변경
        idx += 1
        res += 1
        continue
    if field[nx][ny] != 0: # 이미 다른 값이 들어 있을 때 방향 변경
        idx += 1
        res += 1
        continue
    cnt += 1
    field[nx][ny] = cnt
    if cnt == M*N:
        que.append(nx+1)
        que.append(ny+1)
    x = nx
    y = ny


print(res)
print(*que)