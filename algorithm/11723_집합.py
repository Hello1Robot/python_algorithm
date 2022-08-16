import sys
input = sys.stdin.readline

N = int(input())
set1 = set()
for _ in range(N):
    A, *val = input().strip().split()
    if A == 'add':
        set1.add(val[0])
    elif A == 'remove':
        set1.discard(val[0])
    elif A == 'check':
        if val[0] in set1:
            print(1)
        else:
            print(0)
    elif A == 'toggle':
        if val[0] in set1:
            set1.remove(val[0])
        else:
            set1.add(val[0])
    elif A == 'all':
        set1 = {i for i in range(1, 21)}

    elif A == 'empty':
        set1 = set()

    