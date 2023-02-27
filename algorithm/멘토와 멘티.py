# 멘토 기준 사전순 정렬
# 멘토가 같으면 멘티는 사전 역순 (귀찮다)
N = int(input())
pairs = [input().split() for _ in range(N)]

print(pairs)
pairs.sort(key = lambda x : (x[0], -x[1]))

# print(pairs)