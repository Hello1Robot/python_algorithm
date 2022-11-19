# 끝 점 겹치는건 안침
# 끝점왜주지?
# 시작점에 1, 끝점에 -1 주고
# 나중에 구간합 하면 될듯?
from sys import stdin; input = stdin.readline
import heapq
N = int(input()) 
# 아니 10억이네? ㅋㅋㅋ;
# 이거 회의실맛나는데?

start_list = []
end_list = []
for _ in range(N):
    stt, end = map(int,input().split())
    start_list.append(stt)
    end_list.append(end)
heapq.heapify(start_list)
heapq.heapify(end_list)
max_len = 0
que = []
while start_list:
    a = start_list[0]
    b = end_list[0]
    
    if a < b:
        que.append(heapq.heappop(start_list))
        if len(que) > max_len:
            max_len = len(que)
    else:
        heapq.heappop(end_list)
        que.pop()

print(max_len)