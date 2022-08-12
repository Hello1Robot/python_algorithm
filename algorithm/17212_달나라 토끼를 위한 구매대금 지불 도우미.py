N = int(input())

rst = [0] * (N+8)
rst[1] = 1
rst[2] = 1
rst[3] = 2
rst[4] = 2
rst[5] = 1
rst[6] = 2
rst[7] = 1
for i in range(8, N+1):
    a = (rst[i-7]+1)
    b = (rst[i-5]+1)
    c = (rst[i-2]+1)
    d = (rst[i-1]+1)
    rst[i] = min(a, b, c, d)

print(rst[N])