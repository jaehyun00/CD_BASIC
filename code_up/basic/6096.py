board = [list(map(int, input().split())) for _ in range(19)]

roop = int(input())

negative = [list(map(int, input().split())) for _ in range(roop)]

for n in negative:
    hIndex = n[0] - 1
    vIndex = n[1] - 1

    for i in range(19):
        if board[i][vIndex] == 0:
            board[i][vIndex] = 1
        elif board[i][vIndex] == 1:
            board[i][vIndex] = 0

        if board[hIndex][i] == 0:
            board[hIndex][i] = 1
        elif board[hIndex][i] == 1:
            board[hIndex][i] = 0

for b in board:
    print(' '.join(str(s) for s in b))