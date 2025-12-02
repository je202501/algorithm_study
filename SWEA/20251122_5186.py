T = int(input())

for tc in range(1,T+1):
    N = float(input())
    ans = ''

    for i in range(1,13):
        N = N*2
        ans += str(int(N))
        N -= int(N)
        if N % 1 == 0:
            break
        elif i == 12:
            ans = 'overflow'

    print(f'#{tc} {ans}')