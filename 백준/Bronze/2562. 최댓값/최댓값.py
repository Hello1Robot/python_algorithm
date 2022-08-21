max = 0
max_idx = 0
for i in range(1,10):
    N = int(input())
    if N > max:
        max = N
        max_idx = i
print(max)
print(max_idx)