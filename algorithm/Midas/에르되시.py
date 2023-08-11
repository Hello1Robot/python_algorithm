# 트리 만들어서
# 5 이하의 거리를 다 세는건가보다
# 그럼 BFS 나 DFS로 가면 될 듯?
# 그래서 에르되시부터 출발해서 6이 될 때 까지.
# 집합의 수니까 6 이하인 거 뻗으면서 다 세면 될 듯?
# 처음은 0으로 시작. 에르되시 혼자만 있는 걸 포함하는 건 말이 안되니까? xx 포함이네. 1로 시작
# 아닌가? 6 이하가 되야 함 = 5까지만 구함 일 듯? 5 + 1 = 6

# tree 먼저 만들어야 하네
# 방문처리 문제만 있네.
# 방문처리를 어떻게 할까?
# BFS로 하면 방문처리가 조금 귀찮을 수도 있을까? 흠. 각자가 방문 집합을 가지는 건 너무 손핸데
# 방문처리 좀 이쁘게 어떻게 할까... 흠
# 왔던 곳만 못감. 안갔던 곳은 다 갈 수 있어야 함
# 그리고 갈 때마다 카운트 더해줘야 함
# 흠... 카운트도 글로벌로 해서 논로컬 어쩌구 해야하는데
# 논로컬로 카운트 하면 될 것
# 재귀범위를 넘어설 수도 있을까?
# 그러진 않을듯. 한번에 큐에 다 들어가는 형식은 아니라서
# 순회하는거라서, 문제는 크게 없을 것

# 아니 252 도대체 머임???
# 공동작업동료집합의 경우의 수??? 이게 도대체 머임?

# 저거 왜 6C5임??





from collections import defaultdict

nodes = defaultdict(list)
visited = defaultdict(int)
answer = 1
authors = [["erdos","justi"],["justi","cehui"],["cehui","jhnah"],["jhnah","aaaaa"],["aaaaa","bbbbb"],["bbbbb","ccccc"],["ccccc","ddddd"],["ccccc","ddddd"]]


for a1, a2 in authors:
    nodes[a1].append(a2)
    nodes[a2].append(a1)

visited = defaultdict(int)
visited["erdos"] = 1

print(nodes)
def DFS(now, cnt):
    global answer

    if cnt > 5:
        return
    
    for a in nodes[now]:
        if not visited[a]:
            visited[a] += 1
            answer += 1
            DFS(a, cnt+1)
            visited[a] -= 1
    
DFS("erdos", 0)


print(answer)
