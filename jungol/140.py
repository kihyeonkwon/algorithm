numList = list(map(int, input().split()))

sum = 0
count = 0

for num in numList:
    if num == 0 :
        break
    else:
        sum += num
        count += 1

avg = int(sum / count)

print(sum, avg)