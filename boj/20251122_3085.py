
N = int(input())
board = [list(input()) for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(N-1):
        board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
        for i in range(N):
            pre_x = ''
            pre_y = ''
            cnt_x = 1
            cnt_y = 1
            for j in range(N):
                if pre_x == board[j][i]:
                    cnt_x += 1
                else:
                    pre_x = board[j][i]
                    cnt_x = 1
                if pre_y == board[i][j]:
                    cnt_y += 1
                else:
                    pre_y = board[i][j]
                    cnt_y = 1
                if cnt_x > ans:
                    ans = cnt_x
                elif cnt_y > ans:
                    ans = cnt_y
        board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]

for y in range(N-1):
    for x in range(N):
        board[y][x], board[y+1][x] = board[y+1][x], board[y][x]
        for i in range(N):
            pre_x = ''
            pre_y = ''
            cnt_x = 1
            cnt_y = 1
            for j in range(N):
                if pre_x == board[j][i]:
                    cnt_x += 1
                else:
                    pre_x = board[j][i]
                    cnt_x = 1
                if pre_y == board[i][j]:
                    cnt_y += 1
                else:
                    pre_y = board[i][j]
                    cnt_y = 1
                if cnt_x > ans:
                    ans = cnt_x
                elif cnt_y > ans:
                    ans = cnt_y
        board[y][x], board[y + 1][x] = board[y + 1][x], board[y][x]

print(ans)