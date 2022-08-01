N = input()
alp_dict = {}
for n in N:
    if n in alp_dict:
        alp_dict[n] += 1
    else:
        alp_dict[n] = 1
odd_cnt = 0
alp_tuple = sorted(alp_dict.items())
alp_dict2 = {k:v for k,v in alp_tuple}
res_string = ''
odd_string = ''
if len(N) % 2 == 1:
    for k, v in alp_dict2.items():
        if odd_cnt == 2:
            print("I'm Sorry Hansoo")
            exit()
        if v % 2 == 0:
            res_string += k * (v//2)
        else:
            odd_cnt += 1
            res_string += k * (v//2)
            odd_string += k
    print(res_string+ odd_string +res_string[::-1])
else:
    for k, v in alp_dict2.items():
        if v % 2 == 1:
            print("I'm Sorry Hansoo")
            exit()
        else:
            res_string += k * (v//2)
    print(res_string + res_string[::-1])