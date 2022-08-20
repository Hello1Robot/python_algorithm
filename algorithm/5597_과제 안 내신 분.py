stu_dict = {k:0 for k in range(1,31)}

for i in range(28):
    a = int(input())
    stu_dict[a] += 1

for ky, val in stu_dict.items():
    if val == 0:
        print(ky)