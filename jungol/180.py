def bubblesort(numbers, n):
    for i in range(n):
        for j in range(0, 7 - 1):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = tmp



numbers = list(map(int, input().split()))

bubblesort(numbers, 3)

for number in numbers:
    print(number, end= ' ')
