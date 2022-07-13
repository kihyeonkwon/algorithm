a= input()

LETTERS = 0
DIGITS =0


for i in a:
    if 'a'<=i<='z':
        LETTERS+=1
    elif i.isdigit() :
        DIGITS +=1 

print('LETTERS {0}'.format(LETTERS))
print('DIGITS {0}'.format(DIGITS))