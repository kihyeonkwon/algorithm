data = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
search = 'aeiou'

result = [i for i in data if i not in search]

print(''.join(result))















# sentencestr='Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

# sentence=list(sentencestr)



# numa=int(sentence.count('a'))
# nume=int(sentence.count('e'))
# numi=int(sentence.count('i'))
# numo=int(sentence.count('o'))
# numu=int(sentence.count('u'))

# for i in range(numa):
#     sentence.remove('a')

# for i in range(nume):
#     sentence.remove('e')

# for i in range(numi):
#     sentence.remove('i')

# for i in range(numo):
#     sentence.remove('o')

# for i in range(numu):
#     sentence.remove('u')


# result = ""

# for ele in sentence:
#     result += ele



# print(result)