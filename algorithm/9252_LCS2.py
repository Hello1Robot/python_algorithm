N = list(input()) # [A,C,A,Y,K,P]
N.insert(0,0) # 계산 편의상 첫번째 줄 만들기 위해 임의의 값 넣음
M = list(input()) # [C,A,P,C,A,K]
M.insert(0,0)
field = [[0]*(len(N)) for _ in range(len(M))] # 필드 만들기
value_field = [[0]*(len(N)) for _ in range(len(M))]
max_cnt = 0 # 최대값 셀 카운터 생성
res_str = ''
for i in range(1,len(M)): # 0번 인덱스는 계산안하는 곳이라 비워둠 
    for j in range(1,len(N)): # 위와 동일
        if M[i] == N[j]: # 만약 둘의 값이 같다면
            field[i][j] = field[i-1][j-1] + 1 # 대각선위치 확인해서 값 더해주기
            if field[i-1][j-1] != 0: # 만약 0이 아니면
                value_field[i][j] = str(value_field[i-1][j-1]) + M[i] # 대각선에 담긴 값에 자신 더해줌
            else:
                value_field[i][j] = M[i] # 만약 0이면 자신의 값 더해줌
            if max_cnt < field[i][j]: # 맥스카운트 확인
                max_cnt = field[i][j]
                res_str = value_field[i][j]
        else:
            # 같지 않았을 때의 처리
            # 최장공통문자열과는 달리 최장공통부분수열은 연속되지 않아도 됨
            # 그렇기 때문에 자신의 왼쪽이나 위를 확인해서 같은 값을 집어넣어줌
            if field[i-1][j] > field[i][j-1]:
                field[i][j] = field[i-1][j]
                value_field[i][j] = value_field[i-1][j]
            else:
                field[i][j] = field[i][j-1]
                value_field[i][j] = value_field[i][j-1]
            # field[i][j] = max(field[i-1][j], field[i][j-1])
print(max_cnt)
if max_cnt:
    print(res_str)