while True:
    base = int(input("Base = "))
    height = int(input("Height = "))
    area = round(base * height/2, 1)
    print("Triangle width = %.1f"%(area))
    cont = input("Continue? ").strip()
    if cont =='y' or cont =='Y':
        continue
    else:
        break