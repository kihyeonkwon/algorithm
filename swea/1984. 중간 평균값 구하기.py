tc= int(input())

for i in range (1, tc+1):
    num_list =  list(map(int, input().split()))
    num_list.remove(min(num_list))
    num_list.remove(max(num_list))
    result =  int(round(sum(num_list)/len(num_list), 0))
    print(f'#{i} {result}')
