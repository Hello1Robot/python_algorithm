import heapq

def solution(jobs):
    sjf = []    # 작업 스케쥴러
    for job in jobs:
        heapq.heappush(sjf, job) # 시간순으로 힙큐 정렬
    time = 0 # 현재 시간
    total = 0 # 총 작업시간
    que = [] # 작업 가능한 것들만 넣어 두는 Ready Que
    while sjf or que:
        while sjf and sjf[0][0] <= time:
            a, b = heapq.heappop(sjf)
            heapq.heappush(que, (b,a))

        if not que:
            a, b = heapq.heappop(sjf)
            heapq.heappush(que, (b,a))
        
        cost, start = heapq.heappop(que)
        total += max(0, time-start) + cost
        time = max(time, start) + cost

    return total // len(jobs)