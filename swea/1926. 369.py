x = int(input())


for n in range (1, x+1):
    c3 = (str(n).count('3'))
    c6 = (str(n).count('6'))
    c9 = (str(n).count('9'))

    total = c3+c6+c9

    if total == 0:
        print(n, end=' ')
    else :
        print('-'*total, end=' ')
