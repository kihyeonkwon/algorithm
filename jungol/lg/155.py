letters = 'JUNGOL'

letter = input().strip()

printed = False
for i in range(len(letters)):
    if letters[i] == letter:
        print(i)
        printed=True

if printed == False:
    print('none')