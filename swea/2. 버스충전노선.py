import sys
sys.stdin = open("버스충전input.txt")
tc = int(input())

for i in range (1, tc+1):
    K, N, M = list(map(int, input().split()))
    stops = [0]*N
    gas_stops = list(map(int, input().split()))
    for j in gas_stops:
        stops[j]=1


    location = 0
    movement = 0
    while location + K < N:
        for k in range (location +K, location, -1):
            if stops[k]==1:
                location = k
                movement +=1
                break
            
            elif k==location+1:
                movement = 0
                location = N
                break

    print ("#%d %d"%(i, movement))


