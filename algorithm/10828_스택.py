import sys
rst = []

N = int(input())

for _ in range(N):
    cmd, *val = sys.stdin.readline().strip().split()
    val = int(*val)
    if cmd == 'push':
        rst.append(val)
    elif cmd == 'top':
        if rst:
            print(rst[-1])
        else:
            print(-1)
    elif cmd == 'pop':
        if rst:
            print(rst.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(rst))
    else:
        if rst:
            print(0)
        else:
            print(1)