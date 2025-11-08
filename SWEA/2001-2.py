T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1) prefix 배열 (1-indexed)
    prefix = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = arr[i-1][j-1] \
                + prefix[i-1][j] \
                + prefix[i][j-1] \
                - prefix[i-1][j-1]

    # 2) M×M 최대 부분합 탐색
    result = 0
    for i in range(1, N - M + 2):
        for j in range(1, N - M + 2):
            x2, y2 = i + M - 1, j + M - 1
            total = prefix[x2][y2] \
                - prefix[i-1][y2] \
                - prefix[x2][j-1] \
                + prefix[i-1][j-1]
            result = max(result, total)

    print(f"#{tc} {result}")