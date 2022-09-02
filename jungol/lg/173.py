def sqaure_gap(a, b):
    return abs(a**2 - b**2)

a, b = map(int, (input().split()))

print(sqaure_gap(a, b))