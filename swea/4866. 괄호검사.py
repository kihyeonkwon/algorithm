# import sys
# sys.stdin = open("괄호검사input.txt")




def scan(text):
    stack = []
    left = ['{', '(']
    right = ['}', ')']
    for i in text:
        if i in left:
            stack.append(i)
        elif i in right:
            if len(stack) == 0:
                return 0
            else:
                if left[right.index(i)] == stack.pop():
                    pass
                else:
                    return 0
        else:
            pass


    if stack:
        return 0
    else:
        return 1


total_tc =int(input())

for tc in range(1, total_tc+1):
    b = input()
    print('#%d %d'%(tc, scan(b)))
