import sys
sys.stdin = open('1486.txt')


def powerset(n, k, height_sum):
    global pretty_close
    global pretty_close_list
    if n == k:
        if pretty_close > height_sum-B and height_sum>=B:
            pretty_close = height_sum-B
            pretty_close_list.append(pretty_close)
    else:
        if height_sum-B > pretty_close:
            return False
        else:
            tf_list[k] = 1
            powerset(n, k + 1, height_sum + heights[k])
            tf_list[k] = 0
            powerset(n, k + 1, height_sum)

    return min(pretty_close_list)


total_tc = int(input())

for tc in range(1, total_tc+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    tf_list = [0]*N
    pretty_close_list=[]
    pretty_close = 1000000
    print('#%d %d'%(tc, powerset(N, 0, 0)))
