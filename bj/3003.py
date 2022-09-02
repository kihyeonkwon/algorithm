
# 현재 가지고 있는 킹, 퀸, 룩, 비숍, 나이트, 폰의 수를 입력 받습니다.
king, queen, rook, bishop, knight, pawn = map(int, input().split())


# 킹은 한개만 필요 그렇다면 1 - king 을 해주면 추가로 필요하거나 남는 갯수가 나옵니다!
king = 1 - king

# 퀸도 마찬가지
queen = 1 - queen

# 룩, 비숍 나이트는 두개가 필요하므로 2 - 현개 가진 갯수를 해주면 추가로 필요하거나 남는 갯수
rook = 2 - rook
bishop = 2 - bishop
knight = 2 - knight

# 폰은 8개이므로
pawn = 8 - pawn


# 끝으로 결과물 프린트 하면 끝!
print(king, queen, rook, bishop, knight, pawn)
