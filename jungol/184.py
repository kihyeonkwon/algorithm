letters = input()

alp = 'abcdefghijklmnopqrstuvwxyz1234567890'


for letter in letters:
    letter = letter.lower()
    if letter in alp:
        print(letter, end='')