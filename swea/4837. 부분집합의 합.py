import sys
sys.stdin = open('부분input.txt')

total_tc = int(input())

for tc in range (1, total_tc+1):
    N, K = list(map(int, input().split()))
    mother_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    total_subset=[]
    for i in range (1, 1<<len(mother_list)):
        temp_subset=[]
        for j in range (len(mother_list)):
            if i & (1<<j):
                temp_subset.append(mother_list[j])

        total_subset.append(temp_subset)


    count = 0
    for k in total_subset:
        if len(k) == N and sum(k)==K:
            count+=1
    print("#%d %d"%(tc, count))

