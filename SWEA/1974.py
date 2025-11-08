T=int(input())


def check(a):
    a = sorted(a)

    for i in range(len(a)):
        if i+1 != a[i]:
            return 0
    return 1

for tc in range(1,T+1):
    sudocu = []
    nemo = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    result = 1
    for i in range(9):
        temp = list(map(int,input().split()))
        sudocu.append(temp)

    #가로 확인
    for x in range(9):
        garo = []
        for y in range(9):
            garo.append(sudocu[x][y])

        if check(garo) == 0:
            result = 0
            break

    #세로 확인
    if result == 1:
        for y in range(9):
            sero = []
            for x in range(9):
                sero.append(sudocu[x][y])

            if check(sero) == 0:
                result = 0
                break

    #3*3 확인
    if result == 1:
        for x,y in nemo:
            nemo_ck = []
            for i in range(3):
                for j in range(3):
                    nemo_ck.append(sudocu[x+i][y+j])

            if check(nemo_ck) == 0:
                result = 0
                break

    print(f"#{tc} {result}")
