inputNums = map(int, input().split())

print(inputNums)
odd = 0
even = 0

for i in inputNums:
    if i == 0 :
        break
    elif i%2 == 0:
        even += 1
    else:
        odd += 1

print("odd : %d"%(odd))
print("even : %d"%(even))