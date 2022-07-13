import sys
sys.stdin = open('4013.txt')

TC = int(input())

def clockwise(wheel):
    a = wheel.pop()
    wheel.insert(0, a)

def a_clockwise(wheel):
    a = wheel.pop(0)
    wheel.append(a)

def checkspinr(wheel, wheelr, dir):
    if dir == 1:
        if wheel[2] == wheelr[7]:
            return False
        else:
            return True
    elif dir == -1:
        if wheel[2] == wheelr[5]:
            return False
        else:
            return True

def checkspinl(wheel, wheell, dir):
    if dir == 1:
        if wheel[6] == wheell[3]:
            return False
        else:
            return True
    if dir == -1:
        if wheel[6] == wheell[1]:
            return False
        else:
            return True


def spin(wheel_number, dir):
    wheel_tf=[0, 0, 0, 0]
    wheel_tf[wheel_number]=1
    if dir == 1 :
        clockwise(wheels[wheel_number])
        if wheel_number+1 < 4 and wheel_tf[wheel_number+1]==0:
            if checkspinr(wheels[wheel_number], wheels[wheel_number+1], 1):
                spin(wheel_number+1, -1)
    else :
        a_clockwise(wheels[wheel_number])
        if wheel_number-1 >= 0 and wheel_tf[wheel_number-1]==0:
            if checkspinl(wheels[wheel_number], wheels[wheel_number-1], -1):
                spin(wheel_number-1, -1)

TC = 1

for tc in range(1, TC+1):
    K = int(input())
    wheels = [list(map(int, input().split())) for _ in range(4)]
    turns = [list(map(int, input().split())) for _ in range(K)]
    print(wheels)
    spin(turns[0][0], turns[0][1])
    print(wheels)






