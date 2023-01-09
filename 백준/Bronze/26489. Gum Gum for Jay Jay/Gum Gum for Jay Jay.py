res = 0
while True:
    try:
        _ = input()
        res += 1
    except EOFError:
        break

print(res)