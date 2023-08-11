# 좌표를 받아서, 트리를 구성할 수 있는 지 확인하는 문제
# 트리만 구성할 수 있으면 사실상 순회하면 끝나니 쉬울듯? 아님말구 ㅎ
# y좌표를 기준으로 높은 숫자 = 높은 순위의 트리
# 둘 다 내림차순으로 확인하는거니까
# 정렬을 reverse로 하자

from sys import setrecursionlimit; setrecursionlimit(100000)

def preorder(root, nodes):
    if root == None:
        return nodes
    
    nodes.append(root.index)
    preorder(root.left, nodes)
    preorder(root.right, nodes)

    return nodes

def post(root, nodes):
    if root == None:
        return nodes
    
    post(root.left, nodes)
    post(root.right, nodes)
    nodes.append(root.index)

    return nodes

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.x = None
        self.index = None

def solution(nodeinfo):
    root = None
    N = len(nodeinfo)
    for i in range(N):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x:-x[1])

    for node in nodeinfo:
        new_tree = Tree()
        new_tree.index = node[2]
        new_tree.x = node[0]
        
        if root == None:
            root = new_tree
        else:
            now_parent = root
            while True:
                if now_parent.x < new_tree.x: # sort로 인해 내림차순 -> 오른쪽부터
                    if now_parent.right == None:
                        now_parent.right = new_tree
                        break
                    else:   
                        now_parent = now_parent.right   # 차 있을 경우 -> 부모 트리 바꾸기(타고 내려가기)
                else:
                    if now_parent.left == None:
                        now_parent.left = new_tree
                        break
                    else:
                        now_parent = now_parent.left
    
    return [preorder(root, []), post(root, [])]






nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))