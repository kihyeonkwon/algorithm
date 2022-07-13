import sys
sys.stdin = open('input.txt')

total_tc = 10

for tc in range (1, total_tc+1):
    tc_input=int(input())
    a, b = map(int, input().split())

    def sq(x, y):
        n, square = map(int, [x, y])
        if square ==1:
            return n

        else:
            return n*sq(n,square-1)

    print('#'+str(tc)+' ' + str(sq(a,b)))


#
#
# def c(n,m):
#     if m==1:return n
#     return n*c(n,m-1)
# for t in range(10):
#     a=input();n,m=map(int,input().split());print(f'#{t+1}',c(n,m))
