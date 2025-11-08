T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    # 방향: 오른쪽, 아래, 왼쪽, 위 (행 변화, 열 변화)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dir_idx = 0  # 0=right,1=down,2=left,3=up

    r, c = 0, 0
    for val in range(1, N*N + 1):
        snail[r][c] = val
        nr = r + dr[dir_idx]
        nc = c + dc[dir_idx]

        # 다음 칸이 범위를 벗어나거나 이미 채워져 있으면 방향 전환
        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
            dir_idx = (dir_idx + 1) % 4
            nr = r + dr[dir_idx]
            nc = c + dc[dir_idx]

        r, c = nr, nc

    print(f"#{tc}")
    for row in snail:
        print(' '.join(map(str, row)))