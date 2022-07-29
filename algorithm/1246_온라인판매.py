N, M = map(int, input().split())

consumer = [int(input()) for _ in range(M)]
consumer.sort(reverse=True)
total = 0
res_list = []
for i in range(M):
    if (i+1) < N:
        rev = consumer[i]  * (i+1)
    else:
        rev = consumer[i]  * N
    if rev > total:
        total = rev
        res_list.append(consumer[i])
print(res_list[-1], end=" ")
print(total)


