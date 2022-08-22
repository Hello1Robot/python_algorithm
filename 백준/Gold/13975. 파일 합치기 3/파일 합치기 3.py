import heapq

t = int(input())
for _ in range(t):
    N = int(input())
    nums = list(map(int,input().split()))
    heapq.heapify(nums)
    tot = 0 # 비용 넣을 곳 생성
    # 큐에 값 집어넣기
    # 큐 사이즈가 1일 때 까지 하나씩 빼면서 비교하기.
    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        c = a + b
        tot += c
        heapq.heappush(nums, c)
    print(tot)