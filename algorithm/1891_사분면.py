N, num = map(int,input().split())
fours = ''
while num >= 4:
    a, b = divmod(num, 4)
    fours = str(b) + fours
    num = a
fours = str(num) + fours

print(fours)