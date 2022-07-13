a = [1, 2, 3, 4, 3, 2, 1]

x = a

abc=[]


print(a)


b = len(a)


for i in range (0, b):
    for j in range(0, b):
        if int(a[i]) == int(a[j]) and (i!=j):
            abc+=[j]
            

print(abc)
print(x)
