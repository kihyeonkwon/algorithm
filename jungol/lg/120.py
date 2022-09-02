a, b = map(int, input().split())

small = a if a<b else b
big = b if a<b else a
print(big - small)