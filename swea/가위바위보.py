man1 = input()
man2 = input()

if (man1=="가위" and man2=="보") or (man1=="바위" and man2=="가위") or (man1=="보" and man2=="바위"):
    print("Result : Man 1 Win!")


elif (man2=="가위" and man1=="보") or (man2=="바위" and man1=="가위") or (man2=="보" and man1=="바위"):
    print("Result : Man 2 Win!")
else:
    print("Draw")
