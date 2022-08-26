# 직사각형 넓이 구하는 게 쉬우니까
# 두 번 나오는 숫자가 두 개 있는데
# 그 절대값의 차만큼을 빼면 됨
# 아이디어의 문제인가?
# 구현 어떻게 하느냐일 듯?

N = int(input()) # 평방미터에서 자라는 참외의 양
# 동서남북이 1,2,3,4 로 표현되니까 그냥 칸을 만들어둘까?
# 4 가지 케이스
# (1,3)-왼아래 (1,4)-왼위 (2,3)-오른아래 (2,4) - 오른위
# 
rst1 = []
for _ in range(6):
    방향, 길이 = map(int,input().split())
    rst1.append((방향, 길이))

cnt = 0
rs = 0
while True:
    cnt = 0
    for i in range(4):
        if rst1[i][0] == rst1[i+2][0]:
            cnt += 1
            rs = i
    if cnt == 2:
        break
    else:
        x = rst1.pop(0)
        rst1.append(x)

small_square = rst1[rs][1] * rst1[rs+1][1]
square = (rst1[rs-1][1]+rst1[rs+1][1]) * (rst1[rs][1]+rst1[rs+2][1])
res = (square-small_square)*N

print(res)
