inputNums = list(map(int, input().split()))

sum = 0
count = 0

for i in inputNums:
    if i >100 or i < 0:
        break
    else:
        sum += i
        count += 1

avg = round(sum/count, 1)
print("sum : %d"%(sum))
print("avg : %.1f"%(avg))