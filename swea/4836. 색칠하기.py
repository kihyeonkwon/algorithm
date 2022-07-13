import sys
sys.stdin = open('input.txt')

total_tc = int(input())

for tc in range (total_tc):
    number_of_colors = int(input())
    table = [[0 for _ in range (10)] for _ in range (10)]
    for i in range (number_of_colors):
        x1, y1, x2, y2, color = list(map(int,input().split()))
        for j in range (x1, x2+1):
            for k in range (y1, y2+1):
                if color ==1:
                    table[k][j]+=1
                else :
                    table[k][j]+=2
    count=0
    for l in table:
        for m in l:
            if m==3:
                count+=1

    print("#%d %d"%(tc+1, count))
