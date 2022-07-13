import sys
sys.stdin = open('input.txt')

total_tc = 10

for tc in range(1, total_tc+1):
    tc_number=input()
    find=input()
    target_string=input()
    counter = target_string.count(find)
    print('#%d %d'%(tc, counter))