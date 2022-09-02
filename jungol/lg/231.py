N = int(input())

def divby2(N):
    if N ==0:
        return
    divby2(N//2)
    print(N, end= ' ')

divby2(N)