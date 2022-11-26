from sys import stdin; input=stdin.readline

N = int(input())
M = int(input())
# 선수관계 적어둘 리스트
need_dict = {i:[] for i in range(1,N+1)}
# 이전에 필요한 링크 적어둘 리스트
needs = [0] * (N+1)
