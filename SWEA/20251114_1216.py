T = 10
for tc in range(1,T+1):
    test_case = int(input())
    str_ = [input() for _ in range(100)]
    max = 0
    for i in range(100):
        col_i = ''.join(row[i] for row in str_)
        for j in range(100):
            for k in range(j+1,101):
                garo = str_[i][j:k]
                sero = col_i[j:k]
                garo_len = len(garo)
                sero_len = len(sero)
                if garo == garo[::-1] and garo_len>max:
                    max = garo_len
                if sero == sero[::-1] and sero_len>max:
                    max = sero_len

    print(f"#{test_case} {max}")
