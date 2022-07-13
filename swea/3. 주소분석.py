a = input()




protocol = a.find(':')


print("protocol: " + a[0:protocol])



host = a.find('www')
hostend = a.find('com')

print("host: " + a[host:hostend+3])



others = a.rfind("/") +1

print("others: " + a[others:])