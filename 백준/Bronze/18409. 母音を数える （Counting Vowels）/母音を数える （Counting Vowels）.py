rst = ['a','i','u','e','o']
n, word = input(), input()
cnt = 0
for w in word:
    if w in rst:
        cnt += 1
print(cnt)