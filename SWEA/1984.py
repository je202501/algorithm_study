T = int(input())

for tc in range(1,T+1):
    N = list(map(int,input().split()))

    N_min = min(N)
    N_max = max(N)

    sum = 0
    for i in N:
        sum += i

    result = (sum - N_min - N_max)/8

    print(f"#{tc} {round(result)}")