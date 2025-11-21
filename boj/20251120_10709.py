H, W = map(int,input().split())
now = [input() for _ in range(H)]
pre = [[0 for _ in range(W)] for _ in range(H)]


for i in range(H):
    cloud = -1
    for j in range(W):
        if now[i][j] == 'c':
            cloud = 0
        elif now[i][j] == '.' and cloud != -1:
            cloud += 1
        pre[i][j] = cloud

for lst in pre:
    print(*lst)
