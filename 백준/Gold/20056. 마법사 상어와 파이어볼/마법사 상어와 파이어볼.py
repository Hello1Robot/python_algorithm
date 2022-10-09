# 힙큐를 써서 이동지점 넣어놓고
# 최소값 꺼내서 이전거랑 같은 지 확인하고
# 같으면 합치고 나눠서 스택에 넣기
# 이러면 필드 안써도 됨 ㅎ
import heapq

N, M, K = map(int,input().split()) # NxN, 파이어볼 갯수, 명령횟수
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
stk = []
que = []
# x, y, 크기, 속력, 방향 으로 제시됨
for _ in range(M):
    x, y, p, r, i = map(int,input().split())
    stk.append((x-1, y-1, p, i, r)) # 스택에 값 그대로 넣기
for _ in range(K): # k번 반복하기

    while stk:
        x, y, p, i, r = stk.pop() # 값 꺼내서 이동하기
        nx = (x + (dx[i]*r))% N
        ny = (y + (dy[i]*r))% N
        heapq.heappush(que, (nx, ny, p, i, r))

    while que:
        x, y, p, i, r = heapq.heappop(que)
        cnt = 0
        flag = 0
        while que:
            if x == que[0][0] and y == que[0][1]:
                x2, y2, p2, i2, r2 = heapq.heappop(que)
                if i%2 != i2%2:
                    flag = 1
                p += p2
                r += r2
                cnt += 1
            else:
                break
        if cnt:
            new_p = p//5
            new_r = r//(cnt+1)
            if new_p == 0:
                continue
            if flag:
                for ii in (1,3,5,7):
                    stk.append((x,y,new_p, ii, new_r))
            else:
                for ii in (0,2,4,6):
                    stk.append((x,y,new_p, ii, new_r))
        else:
            stk.append((x,y,p,i,r))

tot = 0
while stk:
    x, y, p, i, r = stk.pop()
    tot += p

print(tot)
