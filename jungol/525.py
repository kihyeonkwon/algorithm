a, b, c = map(int, input().split())

print(f"{1 if (a>b and a>c) else 0} {1 if (a==b and b==c) else 0}")