# 1은 666
# 2~10 은 1666~9666
# 6661 6662 6663 6664 6665 6666 6667... 생각해야됨
# 숌숌숌
# 이걸로 통과하면 양은진 화날듯

N = int(input())

cnt = 0
start = 666
while cnt < N:
    if '666' in str(start):
        cnt += 1
    start += 1

print(start-1)