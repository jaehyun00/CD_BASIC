# 개미집
board = [list(map(int, input().split())) for _ in range(10)]

x = 1
y = 1

while True:
    # 현재 위치
    if board[y][x] == 0:
        board[y][x] = 9
    elif board[y][x] == 2:
        board[y][x] = 9
        break

    # 다음 위치
    if board[y][x + 1] != 1:
        x += 1
    elif board[y + 1][x] != 1:
        y += 1
    else:
        break

for b in board:
    print(' '.join(str(s) for s in b))