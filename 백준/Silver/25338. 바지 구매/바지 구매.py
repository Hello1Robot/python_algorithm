# 그냥 공식 그대로 쓰자
a, b, c, d = map(int,input().split())
N = int(input())
cnt = 0
for _ in range(N):
    y, x = map(int,input().split())
    하체둘레 = max(a*((x-b)**2)+c, d)
    
    if 하체둘레 == y:
        cnt += 1
print(cnt)