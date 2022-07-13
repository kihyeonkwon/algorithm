a, b, c = map(int, input().split())

min_val = a if a<b else b
min_val = min_val if min_val < c else c
print(min_val)