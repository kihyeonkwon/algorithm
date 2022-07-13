n = int(input())


for i in range (1, n+1):
    target = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    result =set()
    x= input()
    a =0
    c = 1
    while a <1:
        y = str(int(x)*c)
        for j in y:
            result.add(int(j))



        if result == target:
            a=1

        else:
            c=c+1
    
    print(f'#{i} {c*int(x)}')
    



