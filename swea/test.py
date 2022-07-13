
import sys
sys.stdin = open('4366.txt')

for testcase in range(int(input())):
    B = input() # Binary
    T = input()  # Ternary

    Binary_arr = []
    Ternary_arr = []

    for i in B:
        Binary_arr.append(int(i))
    for i in T:
        Ternary_arr.append(int(i))




    # 여기까지가 2진수, 3진수를 입력받아 (1, 0, 1, 0)과 (2, 1, 2)로 만들어주는 것
    Binary_num =[]
    Ternary_num = []

    for l in range(len(Binary_arr)):
        if Binary_arr[l] == 1:
            Binary_arr[l] = 0
        else:
            Binary_arr[l] = 1

        B_S = 0
        for n in range(len(Binary_arr)):
            B_S += Binary_arr[n] * (2 ** (len(Binary_arr) - 1 - n))

        Binary_num.append(B_S)


        if Binary_arr[l] == 1:
            Binary_arr[l] = 0
        else:
            Binary_arr[l] = 1



    # 여기까지가 2진수의 자릿수마다 0과 1로 변형해서 나올 수 있는 숫자들의 조합을 10진수로 바꾼것


    for l in range(len(Ternary_arr)):
     # 0이면 1으로, 1이면 2으로, 2이면 0으로. 212
        for m in range(2):
            if Ternary_arr[l] == 0:
                Ternary_arr[l] = 1
            elif Ternary_arr[l] == 1:
                Ternary_arr[l] = 2
            elif Ternary_arr[l] == 2:
                Ternary_arr[l] = 0
            T_S = 0
            # print(Ternary_arr)
            for n in range(len(Ternary_arr)):
                T_S += Ternary_arr[n] * (3 ** (len(Ternary_arr) - 1 - n))
                # print(f'T_S: {T_S}')
            Ternary_num.append(T_S)

        if Ternary_arr[l] == 1:
            Ternary_arr[l] = 2
        elif Ternary_arr[l] == 2:
            Ternary_arr[l] = 0
        elif Ternary_arr[l] == 0:
            Ternary_arr[l] = 1



        # 여기까지가 3진수의 자릿수마다 0과 1, 2로 변형해서 나올 수 있는 숫자들의 조합을 10진수로 바꾼것

    # 2진수와 3진수의 합의 조합 중에서 일치하는 것이 있으면 출력
    for x in range(len(Binary_num)):
        for y in range(len(Ternary_num)):
            if Binary_num[x] == Ternary_num[y]:
                print(f'#{testcase + 1} {Binary_num[x]}')