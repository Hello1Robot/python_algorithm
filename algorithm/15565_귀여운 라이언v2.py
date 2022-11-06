# 한칸씩 right 전진시키기
# 전진시키면서 라이언놈 숫자 카운팅
# 만약 K에 도달하면 길이 저장
# 그런 다음, left 전진시키기
# 전진시키면 길이가 줄어드니까 해당 길이와 현재 길이 min값 저장
# 그러다가 K보다 cnt가 작아지면 다시 right 움직이기
# 그래서 슬라이딩 윈도우가 뭔데...
from sys import stdin; input = stdin.readline

N, K = map(int,input().split())
dolls = tuple(map(int,input().split()))
min_dolls = 1e8
left = 0
right = 0
ryan = 0
if dolls[0] == 1:
    ryan += 1
while right < N:
    # 만약 라이언이 K보다 부족하면
    if ryan < K:
        right += 1
        if right == N:
            break
        if dolls[right] == 1:
            ryan += 1

    # 만약 라이언이 넘쳐흐르면
    else:
        if dolls[left] == 1:
            ryan -= 1
        else:
            min_dolls = min(min_dolls, right-left)

        left += 1
    if left >= right:
        break


if min_dolls == 1e8:
    print(-1)
else:
    print(min_dolls)
        
