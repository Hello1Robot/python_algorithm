burgers = [int(input()) for _ in range(3)]
burgers.sort(reverse=True)
drinks = [int(input()) for _ in range(2)]
drinks.sort(reverse=True)
print(burgers.pop() + drinks.pop() - 50)