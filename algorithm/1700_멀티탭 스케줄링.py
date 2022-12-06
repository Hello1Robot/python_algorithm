from sys import stdin; input=stdin.readline
from collections import deque
from collections import defaultdict

N, K = map(int,input().split())         # 멀티탭이 몇 구인지 나타내는 N, 전자제품의 사용 횟수 K
goods = defaultdict(deque)              # 각 물건의 사용순서를 담아둘 defaultdict 선언
nums = tuple(map(int,input().split()))  # 전자제품의 순서 tuple로 받기
tabs = []                               # 전자제품 꽂아두는 tab
cnt = 0                                 # 갈아끼우는 횟수 담아둘 cnt
for i in range(K):                      # nums 돌면서 나오는 인덱스를 goods에 채우기
    goods[nums[i]].append(i)

for i in range(K):                      
    if nums[i] in tabs:                 # 이미 꽂혀있다면 옮길 필요 없음
        goods[nums[i]].popleft()        # goods에선 꺼내줌
        continue
    if len(tabs) != N:                  # 아직 공간이 남아있으면
        tabs.append(nums[i])            # 꽂아주면 됨
        goods[nums[i]].popleft()
    else:                               # 공간이 없을 경우의 알고리즘 구현
        latest = -1                     # 가장 늦게 꽂는 순서
        latest_num = -1                 # 가장 늦게 꽂는 전자제품
        for n in tabs:                  # 돌면서 가장 늦게 꽂는 전자제품 확인하기
            if goods[n]:
                next = goods[n][0]
                if next > latest:
                    latest = next
                    latest_num = n
            else:                       # 만약에 goods가 비어있으면, 더 이상 쓰지 않는 전자제품이기 때문에 우선적으로 빼기
                latest_num = n
                break
        tabs.remove(latest_num)         # 가장 늦게 꽂는 전자제품 리스트에서 꺼내기
        tabs.append(nums[i])            # 새로 꽂아야 되는 전자제품 꽂기
        goods[nums[i]].popleft()
        cnt += 1

print(cnt)
