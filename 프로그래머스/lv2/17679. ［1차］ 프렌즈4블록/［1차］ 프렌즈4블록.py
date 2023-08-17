def spin_list(rst):
    tup = zip(*rst[::-1])
    return [list(x) for x in tup]

def solution(m, n, board): # m : x축, n : y축. 여기서는 회전시키므로 바꿔서 사용
    field = spin_list(board)
    answer = 0
    while True:
        flag = False
        visited = [[0]*m for _ in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                if field[i+1][j+1] != 0 and field[i][j] == field[i+1][j] == field[i][j+1] == field[i+1][j+1]:
                    visited[i][j] = 1
                    visited[i+1][j] = 1
                    visited[i][j+1] = 1
                    visited[i+1][j+1] = 1
                    flag = True
        
        if not flag:
            break
        
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    field[i][j] = -1
                    field[i].append(0)
                    answer += 1

            field[i] = [x for x in field[i] if x != -1]
        

    return answer