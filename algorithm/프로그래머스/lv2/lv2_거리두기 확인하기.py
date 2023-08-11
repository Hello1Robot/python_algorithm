# 파이썬이라면, 그냥 각 P에 대해 BFS를 돌릴 듯.
# 근데 BFS라고 하니까, 온 방향은 제외해야 해서
# 그럼 그거 추가해도 되긴 해? 온 방향만 추가하면 visited도 필요없는거아닌가?

dr = [(0,1),(1,0),(0,-1),(-1,0)]

def BFS(field):
    que = []
    for i in range(5):
        for j in range(5):
            if field[i][j] == 'P':
                que.append((i,j,-1))
    level = 0
    while que and level < 2:
        new_que = []
        for x,y,d in que:
            for i in range(4):
                if d == i:
                    continue
                nx, ny = x+dr[i][0], y+dr[i][1]
                if nx >= 5 or nx < 0 or ny >= 5 or ny < 0:
                    continue
                if field[nx][ny] == 'P':
                    return 0
                if field[nx][ny] == 'O':
                    new_que.append((nx,ny,(i+2)%4))
        level+=1
        que = new_que

    return 1



def solution(places):
    answer = []
    for p in places:
        answer.append(BFS(p))
    

    return answer

