DP = [0] * 1001
DP[1] = 1
for i in range(2, 1001):
    n = 2
    if DP[i] == 0:
        while True:
            a = i * n
            if a > 1000:
                break
            else:
                DP[a] = 1
            n+=1
N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for n in nums:
    if DP[n] == 0:
        cnt += 1
print(cnt)