chess_pieces = [1, 1, 2, 2, 2, 8]

my_pieces = list(map(int, input().split()))

for i in range(6):
    print(chess_pieces[i] - my_pieces[i], end=" ")
