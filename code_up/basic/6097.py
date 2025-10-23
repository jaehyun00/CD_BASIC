# 세로, 가로
h, w = map(int, input().split())

# 막대기 개수
n = int(input())

# 막대기 길이, 방향(0: 가로, 1: 세로), 좌표 x,y
info = [list(map(int, input().split())) for _ in range(n)]

board = [[0 for _ in range(w)] for _ in range(h)]

for i in info:
    l = i[0]
    d = i[1]
    x = i[3] - 1
    y = i[2] - 1

    for j in range(l):
        if d == 0:
            board[y][x + j] = 1
        elif d == 1:
            board[y + j][x] = 1

for b in board:
    print(' '.join(str(s) for s in b))