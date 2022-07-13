a, b = map(int, input().split())

print(f"{a} > {b} --- {1 if a > b else 0}")
print(f"{a} < {b} --- {1 if a < b else 0}")
print(f"{a} >= {b} --- {1 if a >= b else 0}")
print(f"{a} <= {b} --- {1 if a <= b else 0}")