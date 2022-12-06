from sys import stdin; input=stdin.readline
from collections import deque
from collections import defaultdict

N, K = map(int,input().split())
goods = defaultdict(deque)
nums = tuple(map(int,input().split()))
tabs = []
cnt = 0
for i in range(K):
    goods[nums[i]].append(i)

for i in range(K):
    if nums[i] in tabs:
        goods[nums[i]].popleft()
        continue
    if len(tabs) != N:
        tabs.append(nums[i])
        goods[nums[i]].popleft()
    else:
        latest = -1
        latest_num = -1
        for n in tabs:
            if goods[n]:
                next = goods[n][0]
                if next > latest:
                    latest = next
                    latest_num = n
            else:
                latest_num = n
                break
        if latest_num == -1:
            tabs.pop()
            tabs.append(nums[i])
            goods[nums[i]].popleft()
            cnt += 1
        else:
            tabs.remove(latest_num)
            tabs.append(nums[i])
            goods[nums[i]].popleft()
            cnt += 1

print(cnt)
