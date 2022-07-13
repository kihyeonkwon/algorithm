import sys
sys.stdin = open("input.txt")

total_tc = int(input())

for tc in range (1, total_tc+1):
    tci, n = input().split()
    lookup={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    input_list = list(input().split())
    new_list=[]
    for number in input_list:
        new_list.append(lookup[number])
    new_list.sort()
    new_new_list=[]
    for number in new_list:
        for alp, num in lookup.items():
            if number == num:
                new_new_list.append(alp)
    print(tci)
    for x in new_new_list:
        print(x, end=' ')
    print()