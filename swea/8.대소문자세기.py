a = input()

b = a.upper()

letter = 0

upper = 0

lower = 0

for i in b:
    if i.isalpha():
        letter += 1


num = len(a)

for i in range (num):
    if a[i]!= b[i]:
        lower +=1


upper = letter - lower

print("UPPER CASE {0}".format(upper))
print("LOWER CASE {0}".format(lower))