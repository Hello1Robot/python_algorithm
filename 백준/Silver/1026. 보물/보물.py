# 풀이 아이디어
# A 정방향 B 역방향 정렬
# 서로 곱하기 하면 끝 아닌가???
# B 정렬하지 말라고하긴 했지만
# 무슨문제...?

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
res = 0
for i in range(N):
    res += A[i]*B[i]
print(res)