alphabets = 'abcdefghijklmnopqrstuvwxyz'
word = input()

for alp in alphabets:
    try:
        print(word.index(alp), end=' ')
    except:
        print('-1', end=' ')
