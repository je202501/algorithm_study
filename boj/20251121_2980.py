N, L = map(int,input().split())
info = [[i for i in map(int,input().split())] for _ in range(N)]
loc = 0
cnt = 0
n = 0
while loc != L:
    if n < N and loc == info[n][0]:
        st = cnt % (info[n][1]+info[n][2])
        if st < info[n][1]:
            cnt += info[n][1] - st
        n += 1
    cnt += 1
    loc += 1

print(cnt)
