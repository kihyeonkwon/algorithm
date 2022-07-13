letters = list(input().split())

n = len(letters)

for i in range(n):
    print(letters[n-i-1], end = ' ')