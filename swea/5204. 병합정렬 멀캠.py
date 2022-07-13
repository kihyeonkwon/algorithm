import sys
sys.stdin=open('5204.txt')

TC = int(input())

# def merge(left, right):
#     global count
#     if left[-1] > right[-1]:
#         count += 1
#     result = []
#     i= 0
#     j = 0
#     while i < len(left) or j < len(right):
#         if i < len(left) and  j < len(right):
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#         elif i < len(left):
#             result.append(left[i])
#             i += 1
#         elif j < len(right)  :
#             result.append(right[j])
#             j += 1
#
#     return result

def merge_sort(m):
    if len(m) == 1:
        return m
    left = []
    right = []
    middle = len(m)//2
    for x in range(middle):
        left.append(m[x])
    for x in range(middle, len(m)):
        right.append(m[x])

    left = merge_sort(left)
    right = merge_sort(right)

    global count
    if left[-1] > right[-1]:
        count += 1
    result = [0 for _ in range(N)]
    i= 0
    j = 0
    c = 0
    while i < len(left) and j < len(right):
        if i < len(left) and  j < len(right):
            if left[i] <= right[j]:
                result[c] = (left[i])
                i += 1
            else:
                result[c] = (right[j])
                j += 1
            c += 1

    if i < len(left):
        result[c:] = left[i:]

    if j < len(right)  :
        result[c:] = right[j:]


    return result


for tc in range(1, TC+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    new = merge_sort(numbers)
    print("#%d"%(tc), new[N//2], count)
