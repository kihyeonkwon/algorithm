def abs_sum(numbers):
    sum = 0
    for number in numbers:
        sum += abs(number)
    return sum

numbers = list(map(int, input().split()))

print(abs_sum(numbers))