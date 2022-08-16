import sys
input = sys.stdin.readline

N = int(input())
member = []
for i in range(N):
    age, name = input().split()
    member.append((int(age), i, name))

member.sort(key=lambda x:x[0])

for age, idx, name in member:
    print(age, name)