import sys


sys.stdin = open('5207.txt')

TC = int(input())



def bin_search(N_list, M_list):
    global count
    for target in M_list:
        dir = 'none'
        search(N_list, 0, len(N_list)-1, target, dir)


def search(N_list, l, r, target, dir):
    global count

    if l > r :
        return -1
    else :
        mid = (l+r)//2
        if target == N_list[mid]:
            count += 1
            return 1
        elif target < N_list[mid]:
            if dir == 'left':
                return -1
            dir = 'left'
            return search(N_list, l, mid-1, target, dir)
        else :
            if dir =='right':
                return -1
            dir = 'right'
            return search(N_list, mid+1, r, target, dir)




for tc in range(1, TC+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list.sort()
    count = 0
    bin_search(N_list, M_list)
    # M_list의 원소를 N에서 찾아야 한다.
    print("#%d"%(tc), count)