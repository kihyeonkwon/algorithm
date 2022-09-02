words = input().split()


count = len(words)

for i in range(count):
    print('%d. %s'%(i+1, words[i]))