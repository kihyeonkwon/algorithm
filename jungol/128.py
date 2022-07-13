inputNums = list(map(int, input().split()))


count = 0
for i in inputNums:
    if i ==0:
        break
    elif i%3!=0 and i%5!=0:
        count += 1
    else:
        pass

print(count)