# 소수 두개랑 가장 큰 수 하나 하면 되나?
def gcd(x,y):
    while x:
        x, y = y%x, x
    return y

def lcm(x,y):
    return x*y//gcd(x,y)

T = int(input())
for _ in range(T):
    N = int(input())
    DP = [1]*(N+1)
    sosu = [1]
    for i in range(2,N+1):
        if DP[i] == 1:
            sosu.append(i)
            x = i
            while x <= N:
                DP[x] = 0
                x += i
    res = [sosu[-1], sosu[-2]]
    if N not in res:
        res.append(N)
    else:
        res.append(N-1)
    a, b, c = res
    k = lcm(a,b)
    print(lcm(k,c))

