tc= int(input())


for i in range (1, tc+1):
    N =na = nb = nc = nd = ne = int(input())
    a=0
    b=0
    c=0
    d=0
    e=0

    while True:
        if na%2==0:
            a +=1
            na=na/2
        else:
            break
    while True:
        if nb%3==0:
            b +=1
            nb=nb/3
        else:
            break

    while True:
        if nc%5==0:
            c +=1
            nc=nc/5
        else:
            break

    while True:
        if nd%7==0:
            d +=1
            nd=nd/7
        else:
            break

    while True:
        if ne%11==0:
            e +=1
            ne=ne/11
        else:
            break

    print(f'#{i} {a} {b} {c} {d} {e}')




