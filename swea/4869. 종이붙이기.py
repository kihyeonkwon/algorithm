import sys
sys.stdin = open("종이input.txt")




def papercut(width):
    if width==1:
        return 1
    elif width==2:
        return 3
    return papercut(width - 1) +(2 * papercut(width - 2))







total_tc = int(input())

for tc in range(1, total_tc+1):
    width = (int(input()))//10
    print("#%d %d"%(tc, papercut(width)))
