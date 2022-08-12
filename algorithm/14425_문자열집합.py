N, M = map(int, input().split())
cnt = 0
string_dict = {}
for _ in range(N):
    string_dict[input()] = 0

for _ in range(M):
    m = input()
    if m in string_dict:
        cnt += 1

print(cnt)