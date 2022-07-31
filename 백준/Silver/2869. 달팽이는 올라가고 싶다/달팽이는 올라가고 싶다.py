A, B, V = map(int, input().split())
C = V-A
# C에 도달하면 끝
if C % (A-B) == 0:
    x = C // (A-B)
else:
    x = (C // (A-B))+1
print(x+1) 