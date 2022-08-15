N = int(input())
Ns = list(map(int, input().split()))

M = int(input())
Ms = list(map(int, input().split()))
Ms_dict = {key:0 for key in Ms}
for ns in Ns:
    if ns in Ms_dict:
        Ms_dict[ns] =1
for x in Ms:
    print(Ms_dict[x])
