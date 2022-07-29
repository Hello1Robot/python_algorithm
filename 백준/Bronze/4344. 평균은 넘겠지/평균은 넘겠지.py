import math

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    total = 0
    cnt = 0
    for i in range(1, len(arr)):
        total = total + arr[i]
    avr = total/arr[0]
    for j in range(1, len(arr)):
        if arr[j] > avr:
            cnt += 1

    res = (float(cnt) / float(arr[0]) * 100)
    res2 = round(res, 3)

    print('{0:.3f}%'.format(res2))