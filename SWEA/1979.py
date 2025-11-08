T = int(input())

for tc in range(1,T+1):
    N,K=map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    result = 0

    #가로
    for x in range(N):
        for y in range(N-K+1):
            word = 1
            if y>0 and puzzle[x][y-1] == 1:
                continue
            if y+K < N and puzzle[x][y+K] == 1:
                continue

            for i in range(K):
                if puzzle[x][y+i] == 0:
                    word = 0
                    break
            if word == 1:
                result += 1

    # 세로
    for y in range(N):
        for x in range(N - K + 1):
            word = 1
            if x > 0 and puzzle[x-1][y] == 1:
                continue
            if x + K < N and puzzle[x+K][y] == 1:
                continue

            for i in range(K):
                if puzzle[x +i][y] == 0:
                    word = 0
                    break
            if word == 1:
                result += 1


    print(f"#{tc} {result}")



