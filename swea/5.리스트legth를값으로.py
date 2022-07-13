fruit = ['   apple    ','banana','  melon']
space = ' '
result={}


for i in fruit :
    word =[j for j in i if j not in space]
    word=''.join(word)
    word=str(word)
    result[word] = int(len(word))

print(result)