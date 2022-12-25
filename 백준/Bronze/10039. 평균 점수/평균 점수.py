tot = 0
for _ in range(5):
    x = int(input())
    if x < 40:
        tot += 40
    else:
        tot += x

print(tot//5)