num_set = set()
for _ in range(10):
    num_set.add(int(input()) % 42)

print(len(num_set))