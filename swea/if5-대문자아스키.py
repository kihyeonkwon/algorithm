a = input()

if 'a'<=a<='z':
    print("%s(ASCII: %d) => %s(ASCII: %d)"%(a, ord(a), a.upper(), ord(a.upper())))

elif 'A'<=a<='Z':
    print("%s(ASCII: %d) => %s(ASCII: %d)"%(a, ord(a), a.lower(), ord(a.lower())))
else:
    print(a)