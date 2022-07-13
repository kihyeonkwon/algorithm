letters = input()


while True:
    letters = list(letters)
    num = int(input())-1
    max_num = len(letters)

    if num > max_num-1:
        num = max_num-1
    del(letters[num])
    print(''.join(letters))

    if len(letters) ==1:
        break