nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
new_info = []
for idx, node in enumerate(nodeinfo, 1):
    x, y = node
    new_info.append((y, x, idx))

new_info.sort(reverse=True)
# 이러면 거꾸로 나오는데. 그냥 오른쪽부터 방문하도록 하면 상관없을듯?????
print(new_info)