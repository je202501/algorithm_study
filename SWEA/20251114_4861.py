T=int(input())

for tc in range(1,T+1):
    N,M =map(int,input().split())
    str1 = [input() for _ in range(N)]
    result = ''
    found = False
    for i in range(N):
        col_i = ''.join(row[i] for row in str1)
        for j in range(N-M+1):
            garo = str1[i][j:j+M]
            sero = col_i[j:j+M]
            if garo == garo[::-1]:
                result = garo
                found = True
                break
            if sero == sero[::-1]:
                result = sero
                found = True
                break
        if found:
            break

    print(f"#{tc} {result}")