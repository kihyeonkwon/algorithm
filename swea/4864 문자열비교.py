import sys

sys.stdin = open('input.txt')

total_tc = int(input())

def finder(pattern, text):
    for i in range(len(text) - len(pattern) +1 ):
        count = 0
        for j in range(len(pattern)):
            if text[i+j]==pattern[j]:
                count +=1
        if count == len(pattern):
            return 1


    return 0



for tc in range (1, total_tc+1):
    pattern = input()
    text = input()
    print ('#%d %d'%(tc, finder(pattern, text)))

