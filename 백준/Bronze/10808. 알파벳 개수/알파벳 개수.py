alphabet = [0]*26

st = input()
for s in st:
    a = ord(s) - 97
    alphabet[a] += 1

print(*alphabet)
    