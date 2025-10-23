roop = int(input())

white = [list(map(int, input().split())) for _ in range(roop)]

board = [[0 for _ in range(19)] for _ in range(19)]

for vIndex, vertical in enumerate(board):
    for hIndex, horizontal in enumerate(vertical):
        for i in range(len(white)):
            if white[i][0] - 1 == vIndex and white[i][1] -1 == hIndex:
                board[vIndex][hIndex] = 1

for b in board:
    print(' '.join(str(e) for e in b))