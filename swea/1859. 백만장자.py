total_tc = int(input())

for tc in range (total_tc):
    N = int(input())
    price_list = list(map(int, input().split())) 
    profit = 0
    for i in range (N):
        profit += price_list[i]
        max_price = 0
        for j in range (i, N):
            if max_price <price_list[j]:
                max_price=price_list[j]

        profit -= max_price

    print('#%d %d'%(tc, profit))










# tc = int(input())


# for i in range (1, tc+1):
#     n = int(input())
#     a = list(map(int, input().split()))
#     profit = 0
#     for j in range (n) :
#         maxk=0
#         for k in range (j, n):
#             if a[k] >= maxk:
#                 maxk = a[k]
                
#             else:

#         profit += maxk-a[j]
       
#     print(f'#{i} {profit}')
        


# TC = int(input())
 
# for tc in range(1, TC+1):
#     N = int(input())
#     lst = list(map(int, input().split()))[::-1]
#     margin = 0
#     maxVal = lst[0]
#     for i in range(1, N):
#         if maxVal > lst[i]:
#             margin += maxVal - lst[i]
#         else:
#             maxVal = lst[i]
#     print("#%s"%tc, margin)