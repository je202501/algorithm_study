N, m, M, T, R = map(int,input().split())

result = 0
now_N = 0
m1 = m

if m+T > M:
    print(-1)
else:
    while now_N < N:
        if m+T > M:
            result += 1
            m -= R
            if m < m1:
                m = m1
        else:
            result += 1
            now_N += 1
            m += T
    print(result)