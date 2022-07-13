import sys
sys.stdin = open('input.txt')




def ladder(matrix):
    x, y = matrix[99].index(2) , 99
    while y !=0:
        matrix[y][x] = 0
        if x>=2 and x<=98:
            if matrix[y][x-1]==1:
                x=x-1
            elif matrix[y][x+1]==1:
                x=x+1
            else:
                y = y - 1
        elif x==99:
            if matrix[y][x-1]==1:
                x=x-1
            else:
                y = y - 1
        else:
            if matrix[y][x+1]==1:
                x=x+1
            else:
                y = y - 1


    return x




for i in range (10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    print("#%s %d"%(tc, ladder(matrix)))