# 결국 시간초과 뜸
# LCA의 변형이라고 생각했는데
# 난이도적으로 생각해봐도 아니긴 아닐듯
# 그냥 DFS를 써서 쭈우우우욱 내려가는 걸 고려
# 트리의 순회같은 느낌으로?
# 근데 이게 굳이 양방향일 필요는 없고
# 단방향으로 쭉 내리기 생각하면 될 듯
# 근데 포인트는 1번 + 양 쪽으로 뻗는 포인트만 해야 할 듯
# 전체 포인트 굳이 돌 필요 없고
# 해당 포인트들로 순회하면서 DFS로 양쪽 거리 계산하기

from sys import stdin; input = stdin.readline
from collections import defaultdict

nodes = defaultdict(list)
