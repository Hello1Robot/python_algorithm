N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))
M_dict = {key:0 for key in Ms}
for n in Ns:
    if n in M_dict:
        M_dict[n] += 1

for m in Ms:
    print(M_dict[m], end=' ')
print()