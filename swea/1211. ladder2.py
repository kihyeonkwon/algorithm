import sys
sys.stdin = open('input.txt')




def ladder(matrix):
    min_count = 10000
    max_x, max_y = 0, 0

    for q in range (100):
        count=0

        if matrix[99][q]==1:
            x, y = q, 99
            tf_table=[[False for _ in range(100)] for _ in range(100)]
            while y !=0:
                tf_table[y][x] = True
                count += 1
                if x>=1 and x<=98:
                    if matrix[y][x-1]==1 and tf_table[y][x-1] != True :
                        x=x-1
                    elif matrix[y][x+1]==1 and  tf_table[y][x+1] != True :
                        x=x+1
                    else  :
                        y = y - 1
                elif x==99:

                    if matrix[y][x-1]==1 and tf_table[y][x-1] != True :
                        x=x-1
                    else:
                        y = y - 1
                else:
                    if matrix[y][x+1]==1 and tf_table[y][x+1] != True :
                        x=x+1
                    else:
                        y = y - 1

            if count<=min_count:
                min_count = count
                max_x, max_y = x, y
        else:
            pass


    return max_x




for i in range (10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    print("#%s %d"%(tc, ladder(matrix)))