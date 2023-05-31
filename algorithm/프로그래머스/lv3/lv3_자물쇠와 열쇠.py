# 4번 탐색
# 움직임의 범위 = 2*(M-1) + N 인가? 한번 봐야할듯
# 대각선까지 고려해야 할 듯. 이게 좀 귀찮긴함.
# 결국 범위 넘어가면 컷하고
# 0이나 2 나오면 컷하고 하면 되겠는데
# 문제는 배열 합치는 거. 크기 맞추기가 좀 귀찮을듯
# 크기를 맞추는 것 보다는, 인덱스를 확인하는 게 맞지 않을까? 라는 생각이 듦
# 인덱스를 맞추면 자연스럽게 넘는 것은 컷 될듯? 로직을 그렇게 작성하면 패딩은 필요없을 듯
# 패딩 만들면, 너무 많이 필요할 것 같다는 생각도 들고 뭐 그럼.
# 그럼 범위를 설정할 때, - 부터 + 까지 설정하는 게 맞을 듯. (-(m-1),(-m-1))부터 n+m-1, n+m-1 까지 탐색하도록 할 듯.
# 넘어가는 범위의 경우 계산하지 않도록 구성하기
# 회전하는 게 좀 귀찮을듯. 90도 회전...
# 회전 로직 먼저 짜고, 계산 돌리면 될 듯?
# 배열 일일이 확인하는 거 너무 비효율적이라서
# 구멍 갯수만 세서 채워졌는지 확인하는 게 나을듯?

def solution(key, lock):
    N = len(lock)
    M = len(key)
    holes = 0
    for a in range(N):
        for b in range(N):
            if lock[a][b] == 0:
                holes += 1

    for _ in range(4):
        for i in range(-(M-1),N):
            for j in range(-(M-1),N):
                # 열쇠 위치 확인해서 더하기
                # 움직여야 하는 게 열쇠니까 열쇠를 움직이는 게 맞지 않을까 라는 생각
                # 근데 더했는데 2나 0이 나오면 아예 컷하는 게 맞을 듯(백트래킹)
                fixs = 0
                flag = True # 터졌는지 확인하는 플래그
                for x in range(M):
                    for y in range(M):
                        if i+x < 0 or i+x >= N or j+y < 0 or j+y >= N: # 범위 벗어나면, 열쇠 무시하기
                            continue

                        if lock[i+x][j+y] + key[x][y] == 0 or lock[i+x][j+y] + key[x][y] == 2: # 열쇠 맞췄는데 비거나 겹치면 해당 케이스 종료
                            flag = False
                            break

                        if lock[i+x][j+y] == 0 and key[x][y] == 1: # 열쇠로 빈 곳 채웠을 경우, + 1
                            fixs += 1

                    if not flag: # 케이스 종료
                        break

                if fixs != holes: # 구멍 다 처리했을 경우, 종료
                    continue
                
                return True
            
        key = list(zip(*key[::-1])) # 해당 방향 다 확인했으니까, 90도로 회전시키기

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))