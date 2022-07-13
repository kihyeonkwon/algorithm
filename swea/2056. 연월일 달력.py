i = int (input())

for j in range (1, i+1):
    print(f'#{j}', end=' ')
    a = input()

    if a[4:6] == '01' or a[4:6] == '03' or a[4:6] == '05' or a[4:6] == '07' or a[4:6] == '08' or a[4:6] == '10' or a[4:6] == '12':
        if int(a[6:])<=31:
            print(a[:4] +'/' + a[4:6] +'/' + a[6:])
        else :
            print(-1)

    elif a[4:6] == '04' or a[4:6] == '06' or a[4:6] == '09' or a[4:6] == '11':
        if int(a[6:])<=30:
            print(a[:4] +'/' + a[4:6] +'/' + a[6:])
        else :
            print(-1)

    elif a[4:6] == '02':
        if int(a[6:])<=28:
            print(a[:4] +'/' + a[4:6] +'/' + a[6:])
        else :
            print(-1)

    else:
        print('-1')




# def ispossible(n):
#     m = (int(n)//100)%100
#     d = int(n)%100
#     day = [31,28,31,30,31,30,31,31,30,31,30,31]
#     ans = 0
#     if m>12 or m<1:
#         ans = -1
#     elif 0< d <= day[m-1]:
#         ans = 1
#     else:
#         ans = -1
#     return ans
 
# N = int(input())
 
# for i in range(N):
#     n=input()
#     if ispossible(n) == -1:
#         print(f'#{i+1} -1')
#     else:
#         print(f'#{i+1} {n[0:4]}/{n[4:6]}/{n[6:8]}')



# month_day = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
 
# T = int(input())
# for test_case in range(1, T+1):
#     a = input()
#     year = a[:4] 
#     month = a[4:6] 
#     day = a[6:]
#     if int(month) < 1 or int(month) > 12:
#         print("#{} -1".format(test_case))
#     elif int(day) < 1 or int(day) > month_day[int(month)]:
#         print("#{} -1".format(test_case))
#     else:
#         print("#{} {}/{}/{}".format(test_case,year,month,day))