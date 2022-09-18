from collections import defaultdict

def 전위순회(start):
    if start:
        print(start, end='')
        전위순회(alp[start][0])
        전위순회(alp[start][1])

def 중위순회(start):
    if start:
        중위순회(alp[start][0])
        print(start, end='')
        중위순회(alp[start][1])

def 후위순회(start):
    if start:
        후위순회(alp[start][0])
        후위순회(alp[start][1])
        print(start, end='')

N = int(input())


alp = {}


for i in range(N):
    par, c1, c2 = input().split()
    if c1 == '.':
        c1 = ''
    if c2 == '.':
        c2 = ''
    alp[par] = [c1, c2]

전위순회('A')
print()
중위순회('A')
print()
후위순회('A')
print()