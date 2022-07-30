N = int(input())
students = []
for idx in range(1,N+1):
    students.append(idx)
# 잠시만 생각해보자
# 뺀 수만큼 이동하니까 번호가
# 1부터 N+1 까지 루트를 돌면서
# 위치를 이동시키고
# 그 다음 초기 인덱스 값을 보여주면 된다 ㅇㅋㅇㅋ
sort_nums = list(map(int, input().split()))
res_list = [students[0]]
for i in range(1, N):
    res_list.insert(i-sort_nums[i], students[i])
for j in res_list:
    print(j, end=' ')