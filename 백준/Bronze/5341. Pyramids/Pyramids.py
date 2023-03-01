while True:
    a = int(input())
    if a == 0:
        break
    res = 0
    for i in range(a,0,-1):
        res += i
    print(res)
    