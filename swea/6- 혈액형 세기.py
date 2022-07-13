data=['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
A=0
B=0
AB=0
O=0


for str in data:
    if str=='A':
        A+=1
    if str=='B':
        B+=1
    if str=='O':
        O+=1
    if str=='AB':
        AB+=1


print("{'A': %i, 'O': %i, 'B': %i, 'AB': %i}"%(A, O, B, AB))