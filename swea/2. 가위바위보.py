# trash1= input()
# trash2= input()

# a =input()
# b =input()


# def rps(a, b):
#     if ((a or b) =='가위') and ((a or b) =='바위'):
#         print ('바위가 이겼습니다!')

#     elif ((a or b) =='바위') and ((a or b) =='보'):
#         print('보가 이겼습니다!')

#     elif ((a or b) =='보') and ((a or b) =='가위'):
#         print('가위가 이겼습니다!')

#     elif ((a and b) =='가위') or ((a and b) =='바위') or ((b and a)=='보'):
#         print('비겼습니다!')

# rps(a,b)


player1 = input()
player2 = input()
player1hand = input()
player2hand = input()

game ={'player1':player1hand, 'player2':player2hand}

print(game)

man1 = game['player1']
man2 = game.get('player2')

if (man1=="가위" and man2=="보") or (man1=="바위" and man2=="가위") or (man1=="보" and man2=="바위"):
    print("Result : {0} with {1} Win!".format(player1, game['player1']))


elif (man2=="가위" and man1=="보") or (man2=="바위" and man1=="가위") or (man2=="보" and man1=="바위"):
    print("Result : {0} with {1} Win!".format(player2, game['player2']))
else:
    print("Draw")
