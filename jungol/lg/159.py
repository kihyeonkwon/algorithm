n = int(input())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)
for number in numbers:
    print(number)
