N = int(input())
req = int(input()) # 목표로 할 숫자
cnt = 0
num_list = list(map(int,input().split()))
while num_list:
    x = req - num_list[0]
    if x in num_list:
        cnt += 1
        num_list.remove(x)
        num_list.remove(num_list[0])
    else:
        num_list.remove(num_list[0])
print(cnt)