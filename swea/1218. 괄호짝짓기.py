import sys

sys.stdin = open('input.txt')


def scan(text):
    stack = []
    left = ['{', '[', '(', '<']
    right = ['}', ']', ')', '>']
    result = 1
    for i in text:
        if i in left:
            stack.append(i)
        else:
            if stack ==False:
                return 0

            else:
                if left[right.index(i)] == stack[-1]:
                    stack.pop()
                    result = 1
                else:
                    return 0

    return result


total_tc =10

for tc in range(1, total_tc+1):
    length = int(input())
    b = input()
    print('#%d %d'%(tc, scan(b)))
