num_dict = {x:0 for x in range(10)}
big_num = str(int(input()) * int(input()) * int(input()))
for n in big_num:
    num_dict[int(n)] += 1

for num in num_dict.values():
    print(num)
