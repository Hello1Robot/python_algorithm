# 두개의 뭉치를 합칠 때, 총합만큼 토탈을 증가시킨다.
# 두 개의 뭉치를 합친 후, 넣고 다시 정렬시킨다.
# 정렬시킨 것에서 또 제일 낮은것 두 개.
# 반복해서 1개의 뭉치가 될 때 까지 진행한다.
# 자료구조에 대한 이해가 필요한데
import sys
import heapq
input = sys.stdin.readline

N = int(input())
res = 0
nums = [int(input()) for _ in range(N)]
if N == 1:
    print(0)
    exit()
heapq.heapify(nums)
while len(nums) != 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    c = a + b
    res += c
    heapq.heappush(nums, c)

print(res)