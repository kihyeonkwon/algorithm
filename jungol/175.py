number = int(input())
numbers = list(map(int, input().split()))
for i in sorted(numbers, reverse=True):
    print(i, end=' ')