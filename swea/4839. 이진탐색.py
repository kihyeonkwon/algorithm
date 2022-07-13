import sys
sys.stdin = open("이진input.txt")

def bin_search(l, r, P):
    count = 0
    end=0
    while end==0:
        c = int((l + r) / 2)
        if c>P:
            r = c
            count+=1
        elif c<P:
            l = c
            count+=1
        else:
            count+=1
            end +=1

    return count



total_tc = int(input())


for tc in range (1, total_tc+1):
    l=1
    r, Pa, Pb = list(map(int, input().split()))
    a_count = bin_search(l, r, Pa)
    b_count = bin_search(l, r, Pb)
    if a_count>b_count:
        result = 'B'
    elif a_count < b_count:
        result = 'A'
    else:
        result = 0

    print("#%d %s"%(tc, result))

