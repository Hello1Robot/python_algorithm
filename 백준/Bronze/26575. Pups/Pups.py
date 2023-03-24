T = int(input())
for _ in range(T):
    a, b, c = map(float, input().split())
    print(f"${a*b*c:0.2f}")