from sys import stdin; input=stdin.readline
N, K = map(int,input().split())
nums = list(input().strip())
stk = []
for num in nums:
    if K > 0:
        if stk:
            if stk[-1] >= num:
                stk.append(num)
            else:
                while stk and stk[-1] < num:
                    stk.pop()
                    K -= 1
                    if K == 0:
                        break
                stk.append(num)
        else:
            stk.append(num)

    else:
        stk.append(num)

while K > 0:
    stk.pop()
    K -= 1

print(''.join(stk))

