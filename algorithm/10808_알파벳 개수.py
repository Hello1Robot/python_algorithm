from sys import stdin; input=stdin.readline
alphabet = [0]*26

st = input().rstrip()
for s in st:
    a = ord(s) - 97
    alphabet[a] += 1

print(*alphabet)
    