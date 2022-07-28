# 두개의 뭉치를 합칠 때, 총합만큼 토탈을 증가시킨다.
# 두 개의 뭉치를 합친 후, 넣고 다시 정렬시킨다.
# 정렬시킨 것에서 또 제일 낮은것 두 개.
# 반복해서 1개의 뭉치가 될 때 까지 진행한다.
# 자료구조에 대한 이해가 필요한데
import sys

N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(N))

