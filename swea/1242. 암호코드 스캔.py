import sys

sys.stdin = open('1242.txt')

TC = int(input())


for tc in range(1, TC+1):
    dict = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    N, M= list(map(int, input().split()))
    table=[]
    for _ in range(N):
        line_input = input()
        line_output = []
        for number in line_input:
            line_output.extend(dict[number])
        table.append(line_output)




    codes = []
    for i in range (N):
        for j in range(4*M-1, -1, -1):
            if table[i][j] != '0':
                if table[i-1][j] == '0':
                    while j>0:
                        a = b = c = d = 0
                        for x in range(j, -1, -1):
                            if table[i][x] == '1':
                                c += 1
                            else:
                                break
                        for x in range(j-c, -1, -1):
                            if table[i][x] == '0':
                                b += 1
                            else:
                                break
                        for x in range(j-c-b, -1, -1):
                            if table[i][x] == '1':
                                a += 1
                            else:
                                break
                        for x in range(j-a-b-c, -1, -1):
                            if table[i][x]=='0':
                                d += 1
                            else:
                                break

                        j = j - a - b - c - d
                        div = min(a,b,c)
                        a = int(a / div)
                        b = int(b / div)
                        c = int(c / div)

                        codes.append([a, b, c])

                    break



    decode = {0:[2, 1, 1], 1:[2, 2, 1], 2:[1,2,2], 3:[4,1,1], 4:[1,3,2], 5:[2,3,1], 6:[1,1,4], 7:[3,1,2], 8:[2,1,3], 9:[1,1,2]}

    decodes_multiple = []
    number_of_codes = len(codes)//8
    for i in range (number_of_codes):
        decodes = []
        for j in range(8*i, 8*i+8):
            for num, li in decode.items():
                if codes[j] ==li:
                    decodes.append(num)
        decodes = decodes[::-1]
        decodes_multiple.append(decodes)

    new_decodes_multiple=[]
    for i in decodes_multiple:
        if i not in new_decodes_multiple:
            new_decodes_multiple.append(i)

    #(홀수 자리의 합*3) + 짝수자리의합 + 검증코드(마지막 숫자) 의 합을 구해서 %10을 통해 검증한다.
    def validation(decodes):
        validation_sum = (decodes[0]+decodes[2]+decodes[4]+decodes[6])*3 + decodes[1] + decodes[3] + decodes[5] + decodes[7]
        sum = (decodes[0]+decodes[2]+decodes[4]+decodes[6]) + decodes[1] + decodes[3] + decodes[5] + decodes[7]
        if validation_sum%10 == 0:
            return sum
        else:
            return 0

    result = 0
    for i in range(len(new_decodes_multiple)):
        result += validation(new_decodes_multiple[i])


    print("#%d %d"%(tc, result))


