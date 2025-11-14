T = 10
for tc in range(1,T+1):
    N = int(input())
    str_ = [input() for _ in range(8)]
    result = 0

    for i in range(len(str_)):
        # col_i = ""
        # for row in str_:
        #     col_i += row[i]
        col_i = ''.join(row[i] for row in str_)
        for j in range(len(str_)-N+1):
            garo = str_[i][j:j+N]
            sero = col_i[j:j+N]
            if garo == garo[::-1]:
                result += 1
            if sero == sero[::-1]:
                result += 1

    print(f"#{tc} {result}")