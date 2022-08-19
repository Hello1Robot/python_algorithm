N = int(input())
str_len_list = []

str_list = []
for i in range(N):
    x = input()
    if x not in str_list:
        str_list.append(x)

for i in str_list:
    A = [len(i), i]
    str_len_list.append(A)

rst1 = sorted(str_len_list, key=lambda x:x[1])
rst2 = sorted(rst1, key=lambda x:x[0])
for i in range(len(rst2)):
    print(rst2[i][1])