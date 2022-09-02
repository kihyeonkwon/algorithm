def avg_round(numbers):
    n = len(numbers)
    total_sum = 0
    for number in numbers:
        total_sum += number

    result = round(total_sum/n)
    return result

def round_avg(numbers):
    n = len(numbers)
    total_sum = 0
    for number in numbers:
        total_sum += round(number)

    result = total_sum / n
    return round(result)

numbers = list(map(float, input().split()))
print(avg_round(numbers))
print(round_avg(numbers))