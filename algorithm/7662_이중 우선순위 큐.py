# 힙큐를 이용하는데
# 최소값과 최대값 꺼내는 문제
# cnt를 이용해서 최대값은 킵해뒀다가
# 없애는 걸로 구현하기로 함

# 이중으로 했을 때 반례
# 1
# 7
# I 10
# I 20
# D 1
# I 30
# I 40
# D -1
# D -1
# 40 30
# 이거 일단 해결 못해서 보류

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    # I는 삽입, D는 출력.
    # D가 -1일 때는 최솟값, 1일 때는 최대값
    # 근데 생각해보니까
    # 힙큐 이거...
    # 마지막 수가 최대값인 걸 보장 못해주지 않나?
    # 한번 해봐
    doublemin = []
    doublemax = []
    cnt = 0
    for i in range(N):
        cmd, val = input().split()
        val = int(val)
        if cmd == 'I':
            heapq.heappush(doublemin, val)
            heapq.heappush(doublemax, (-val, val))
            cnt += 1
        else:
            if val == -1:
                if cnt > 0:
                    cnt -= 1
                    heapq.heappop(doublemin)
                    if cnt == 0:
                        doublemax.clear()
            else:
                if cnt > 0:
                    cnt -= 1
                    heapq.heappop(doublemax)
                    if cnt == 0:
                        doublemin.clear()
    if cnt > 0:
        print(heapq.heappop(doublemax)[1], heapq.heappop(doublemin))
    else:
        print('EMPTY')
                    
                
                