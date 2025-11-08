T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    pari = []
    for i in range(N):
        temp = list(map(int,input().split()))
        pari.append(temp)

    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for x in range(i,i+M+1):
                for y in range(j,j+M+1):
                    sum += pari[x][y]
            if result < sum:
                result = sum
    print(f"#{tc} {result}")