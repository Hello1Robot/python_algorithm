# 좌표를 받아서, 트리를 구성할 수 있는 지 확인하는 문제
# 트리만 구성할 수 있으면 사실상 순회하면 끝나니 쉬울듯? 아님말구 ㅎ
# y좌표를 기준으로 높은 숫자 = 높은 순위의 트리
# 둘 다 내림차순으로 확인하는거니까
# 정렬을 reverse로 하자


def solution(nodeinfo):
    answer = [[]]
    N = len(nodeinfo)
    nodes = [0] * (N+1)
    lson = [[] for _ in range(N+1)]
    rson = [[] for _ in range(N+1)]


    return answer



nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))