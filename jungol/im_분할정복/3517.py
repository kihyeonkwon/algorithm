import sys
sys.stdin = open("jungol/im_분할정복/input.txt", "r")


def binarySearchDFS(N_list, low, high, q):
    if low > high:
        return -1

    mid = (high+low)//2
    if N_list[mid] == q:
        return mid

    elif(N_list[mid] > q):
        return binarySearchDFS(N_list, low, mid-1, q)

    else:
        return binarySearchDFS(N_list, mid+1, high, q)


def binarySearchLoop(N_list, low, high, q):
    while low <= high:
        mid = (low + high) // 2
        if N_list[mid] == q:
            return mid
        if N_list[mid] > q:
            high = mid - 1
        else:
            low = mid + 1

    return -1


N = int(input())
N_list = list(map(int, input().split()))
Q = int(input())
Q_list = list(map(int, input().split()))


answer = []
for q in Q_list:
    idx = binarySearchDFS(N_list, 0, N-1, q)
    answer.append(str(idx))

print(" ".join(answer))
