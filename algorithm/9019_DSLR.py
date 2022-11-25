from collections import deque
def BFS(start, end):
    que = deque()
    que.append((start,'')) # 문자열로 받기
    while que:
        x, root = que.popleft()
        if x == end:
            return root
        for i in range(1,5):
            if i == 1:
                
                nx = str((int(x)*2)%10000).zfill(4)
                nroot = root + 'D'

            elif i == 2:
                nx = str(int(x) - 1).zfill(4)
                if nx == '0000':
                    nx = '9999'
                nroot = root + 'S'

            elif i == 3:
                nx = x[1]+x[2]+x[3]+x[0]
                nroot = root + 'L'
            
            else:
                nx = x[3]+x[0]+x[1]+x[2]
                nroot = root + 'R'


            que.append((nx,nroot))



T = int(input())
for _ in range(T):
    A, B = input().split()
    # 그럼 돌면서 str 값 하나씩 들고있어야 할듯
    # 사실 커맨드 저거 안쓰고 range 4 돌면서 값 확인
    print(BFS(A.zfill(4),B.zfill(4)))

