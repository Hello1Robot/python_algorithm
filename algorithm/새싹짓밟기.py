tot = 0
for _ in range(4):
    a = int(input())
    tot += a

x,y = divmod(tot, 60)
print(x)
print(y)