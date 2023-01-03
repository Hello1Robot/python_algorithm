import hashlib

N = input()
result = hashlib.sha256(N.encode()).hexdigest()
print(result)