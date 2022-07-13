a = int(input())


for i in range (1, a+1):
    a, b = map(int, input().split(' '))
    ev = 0
    if a > b:
        ev = '>'
    elif a<b :
        ev = '<'
    else :
        ev = '='
    
    print(f'#{i} {ev}')
    