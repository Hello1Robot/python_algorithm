str1 = list(input())
str1.insert(0, 0)
str2 = list(input())
str2.insert(0,-1)
N = len(str1)
M = len(str2)
max_cnt = 0
field = [[0]*(M) for _ in range(N)]
for i in range(1,N):
    for j in range(1,M):
        if str1[i] == str2[j]:
            field[i][j] = field[i-1][j-1]+1
            if max_cnt < field[i][j]: # 맥스카운트 확인
                max_cnt = field[i][j]
print(max_cnt)