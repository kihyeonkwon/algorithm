import sys

sys.stdin = open("반복문자input.txt")

total_tc = int(input())

def repeat(start):
    n = len(text)
    if start < n-1:
        if text[start] == text[start+1]:
            text.pop(start)
            text.pop(start)
            if start==0:
                return repeat(start)
            return repeat(start-1)
        else:

            return repeat(start+1)
    else:
        return len(text)



for tc in range(1, total_tc+1):
    text = list(input())

    print("#%d %d"%(tc, repeat(0)))



