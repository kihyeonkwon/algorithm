import sys

sys.stdin = open('1240.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    table = [input() for _ in range (N)]

    #마지막 줄 끝점을 찾는다
    for i in range (N):
        for j in range(M-1, -1, -1):
            if table[i][j]=='1':
                end_i = i
                end_j = j
                break


    #7개씩 8개로 자른다. 총 46개란 말이고
    codes = []
    for j in range(end_j-55, end_j+1, 7):
        codes.append(table[end_i][j:j+7])

    #각 배열에 해당하는 숫자를 구한다
    decode = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    decodes=[]
    for code in codes:
        decodes.append(decode[code])

    #(홀수 자리의 합*3) + 짝수자리의합 + 검증코드(마지막 숫자) 의 합을 구해서 %10을 통해 검증한다.
    def validation(decodes):
        validation_sum = (decodes[0]+decodes[2]+decodes[4]+decodes[6])*3 + decodes[1] + decodes[3] + decodes[5] + decodes[7]
        sum = (decodes[0]+decodes[2]+decodes[4]+decodes[6]) + decodes[1] + decodes[3] + decodes[5] + decodes[7]
        if validation_sum%10 == 0:
            return sum
        else:
            return False
    valid_value = validation(decodes)

    #정상이면 합을 출력 비정상이면 0을 출력
    if valid_value:
        result = valid_value
    else :
        result = 0
    print("#%d %d"%(tc, result))
