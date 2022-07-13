import sys
sys.stdin = open("숫자카드input.txt")
tc = int(input())

for i in range (1, tc+1):
    N = int(input())
    deck = []
    cards=input()
    for j in cards:
        deck.append(int(j))

    counting_cards=[0]*10
    for k in deck:
        counting_cards[k]+=1

    max = 0
    number =0
    for l in counting_cards:
        if l >= max:
            max = l
            result = number
        number +=1

    print('#%d %d %d'%(i, result, max))
