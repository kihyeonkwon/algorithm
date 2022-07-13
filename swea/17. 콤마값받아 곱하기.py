from math import pi


a = list(map(int, input().split(', ')))

for i in range (len(a)):
    if i < len(a)-1:
        print('{0:0.2f}'.format(a[i]*pi*2), end=', ')
    else:
        print('{0:0.2f}'.format(a[i]*pi*2))