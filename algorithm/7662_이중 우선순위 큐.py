# 힙큐를 이용하는데
# 최소값과 최대값 꺼내는 문제


from sys import stdin; input = stdin.readline
import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    # I는 삽입, D는 출력.
    # D가 -1일 때는 최솟값, 1일 때는 최대값

    idx = 0
    doublemin = []
    doublemax = []
    popindex = {}
    cnt = 0
    for _ in range(N):
        cmd, val = input().split()
        val = int(val)

        if cmd == 'I':
            heapq.heappush(doublemin, (val, idx))
            heapq.heappush(doublemax, (-val, idx))
            idx += 1
            cnt += 1
        else:
            if val == -1:
                if cnt > 0:
                    cnt -= 1
                    while doublemin:
                        a, b = heapq.heappop(doublemin)
                        if b not in popindex:
                            popindex[b] = 1
                            break
                    


            else:
                if cnt > 0:
                    cnt -= 1
                    while doublemax:
                        a, b = heapq.heappop(doublemax)
                        if b not in popindex:
                            popindex[b] = 1
                            break


    if cnt > 0:
        while True:
            if doublemax[0][1] not in popindex:
                break
            heapq.heappop(doublemax)
            
        while True:
            if doublemin[0][1] not in popindex:
                break
            heapq.heappop(doublemin)

        print(-(heapq.heappop(doublemax)[0]), heapq.heappop(doublemin)[0])
    else:
        print('EMPTY')
