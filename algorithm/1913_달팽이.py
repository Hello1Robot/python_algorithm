# 이동하는 숫자 세보면 1 - 1 - 2 - 2 - 3 - 3 - 4 - 4 - 5 - ... (범위 넘을 때까지.)
# while 안에서 cnt 세면서 2 될 때마다 횟수값 + 1 해줘야 될 듯
N = int(input())
field = [[0]*N for _ in range(N)]
dx = []
dy = []