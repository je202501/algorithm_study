T = int(input())

for tc in range(1,T+1):
    N, hx = input().split()
    N = int(N)
    hx = int(hx, 16)
    bi = bin(hx)[2:]
    bi = bi.zfill(N*4)

    print(f'#{tc} {bi}')