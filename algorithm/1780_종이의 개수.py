# 딱 봐도 재귀로 푸는 문제
# 반갈죽해서 리스트 만들고 반복하면 될 듯
# N값을 리스트에 넣고 계속 자를듯.
# 확인하면서 N//3만큼 확인 범위를 줄여감
# 시작x와 시작y를 재귀함수에 계속 표시함
# 만약 범위가 1이면 세서 넣기
종이세기 = [0,0,0]

N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]

def 종이(x,y,r):
    start = field[x][y]
    if r == 1:
        종이세기[start] += 1
        return
    for i in range(x,x+r):
        for j in range(y,y+r):
            if field[i][j] != start:
                종이(x,y,r//3)
                종이(x+r//3,y,r//3)
                종이(x+(2*r//3),y,r//3)
                종이(x,y+r//3,r//3)
                종이(x,(y+2*r//3),r//3)
                종이(x+r//3,y+r//3,r//3)
                종이(x+r//3,y+(2*r//3),r//3)
                종이(x+(2*r//3),y+r//3,r//3)
                종이(x+(2*r//3),y+(2*r//3),r//3)
                return
    종이세기[start] += 1
    return

종이(0,0,N)
print(종이세기[-1])
print(종이세기[0])
print(종이세기[1])
