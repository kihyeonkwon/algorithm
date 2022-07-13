# x = int(input())

# se = [1, 1]

# for i in range(1, x-1):
#     add = [se[i-1] + se[i]]
#     se += add
# print(se)




x=int(input())

a=0
b=1
c=0

abc=[]

for i in range(1, x+1):
    abc+=[b]
    c=b
    b=a+b
    a=c

print(abc)