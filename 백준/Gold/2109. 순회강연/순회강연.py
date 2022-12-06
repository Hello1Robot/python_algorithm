from sys import stdin; input=stdin.readline
import heapq

N = int(input())

# P와 D가 주어지는데, D순으로 정렬할 거니까 순서 바꿔서 넣어주기
seminar = []
for _ in range(N):
    p, d = map(int,input().split())
    seminar.append((d,p))

seminar.sort() # 날짜순으로 정렬. 생각해보면 key=lambda로 정렬해도 상관없었을듯
que = []

for day, pay in seminar: # seminar 돌면서 날짜와 페이 확인
    heapq.heappush(que, pay) # 일단 큐에 집어넣기
    if day < len(que): # 만약 날짜보다 들어있는 세미나의 양이 많다면
        heapq.heappop(que) # 제일 페이가 낮은 세미나 뽑아내기

print(sum(que))