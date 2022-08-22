N = int(input())
weights = list(map(int, input().split()))
weights.sort()
res = 0
for weight in weights:
    if res+2 <= weight:
        break
    else:
        res += weight
print(res+1)
