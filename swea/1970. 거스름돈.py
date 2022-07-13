tc= int(input())


for i in range (1, tc+1):
    N = int(input())

    a = b = c = d =e =f =g =h = 0

    a = N // 50000
    N = N - 50000*a

    b = N//10000
    N = N - 10000*b

    c = N//5000
    N = N - 5000*c

    d = N//1000
    N = N - 1000*d

    e = N//500 
    N = N - 500*e

    f = N//100 
    N = N - 100*f

    g = N//50 
    N = N - 50*g

    h = N//10 
    N = N - 10*h

    print(f'#{i} \n{a} {b} {c} {d} {e} {f} {g} {h}')

