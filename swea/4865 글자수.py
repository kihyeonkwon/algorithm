import sys

sys.stdin = open('input.txt')


def hmany(target, text):
    target = set(target)
    result_dict ={}
    for i in target:
        result_dict[i]=0
        for j in text:
            if i ==j:
                result_dict[i]+=1
    return max(result_dict.values())





total_tc=int(input())

for tc in range (1, total_tc+1):
    target = input()
    text = input()
    print('#%d %d'%(tc, hmany(target, text)))