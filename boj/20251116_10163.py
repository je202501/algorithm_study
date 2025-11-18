N = int(input())
paper = [[0]*1001 for _ in range(1001)]

loc = [0]*(N+1)
for i in range(1,N+1):
    temp = list(map(int,input().split()))
    loc[i] = temp



for n in range(1,N+1):
    ans_temp = 0
    x,y,x_len,y_len = loc[n]
    for i in range(y,y+y_len):
            paper[i][x:x+x_len] = [n]*x_len

cnt = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        cnt[paper[i][j]] += 1



for i in range(1,len(cnt)):
    print(cnt[i])


