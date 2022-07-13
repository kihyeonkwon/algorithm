import sys
sys.stdin = open('5208.txt')

TC = int(input())

def travel(stations, location, count):
    global min_count
    count += 1
    if count >= min_count:
        return -1
    if location == N:
        min_count = min(min_count, count)
        return 1
    fuel = stations[location]
    for i in range(1, fuel+1):
        if location + i <= N:
            travel(stations, location+i, count)

for tc in range(1, TC+1):
    stations = list(map(int, input().split()))
    N = stations[0]
    min_count = 0xfffffff
    count = 0
    travel(stations, 1, count)
    print("#%d"%(tc), min_count-2)
