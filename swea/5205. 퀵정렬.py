import sys
sys.stdin = open('5205.txt')

TC = int(input())

def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)

def partition(A, l, r):

    o = l
    p = A[o]
    while l < r :
        while A[l] <= p and l < r:
            l += 1
        while A[r] >= p and l <= r:
            r -= 1
        if l < r :
            A[l], A[r] = A[r], A[l]
    A[o], A[r] = A[r], A[o]
    return r



for tc in range(1, TC+1):
    N = int(input())
    A = list(map(int, input().split()))

    quickSort(A, 0, len(A)-1)
    print("#%d"%(tc), A[int(N/2)])
