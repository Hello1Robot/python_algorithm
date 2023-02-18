# 실험포인트
# min_lang이 1이 되면 프린트되고 종료시키면 더 빠를까?

from sys import stdin; input = stdin.readline

N, S = map(int,input().split())
nums = list(map(int, input().split()))
stt, end = 0, 1
min_lang = 1e9
tot = nums[0]
while stt <= end and end <= N :
    
    if tot >= S:
        gap = end - stt
        if gap == 1:
            print(1)
            exit()
        min_lang = min(min_lang, gap)
        tot -= nums[stt]
        stt += 1

    else:
        if end == N:
            break
        tot += nums[end]
        end += 1

[print(min_lang) if min_lang != 1e9 else print(0)]
