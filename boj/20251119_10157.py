C, R = map(int,input().split())
K = int(input())
if K > C*R :
    print(0)
else:
    seat = [[0 for _ in range(C)] for _ in range(R)]

    c_st = 0
    r_st = 0
    c_pt = [0,1,0,-1]
    r_pt = [1,0,-1,0]
    di = 0

    cnt = 0
    for k in range(1, K+1):
        seat[r_st][c_st] = k
        nr = r_st + r_pt[di]
        nc = c_st + c_pt[di]
        if k == K:
            break
        if not (0 <= nr < R and 0 <= nc < C) or (seat[nr][nc] != 0):
            di = (di+1)%4

        r_st += r_pt[di]
        c_st += c_pt[di]

    print(c_st+1, r_st+1)