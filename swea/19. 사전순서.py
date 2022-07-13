

a = list(input().split(', '))

a =sorted(a)

num = len(a)

for i in a :
    if i != a[-1] :
        print('{0}'.format(i), end=', ')
    else :
        print('{0}'.format(i))