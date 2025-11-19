T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    case = []
    for _ in range(N):
        case.append(input())
    ans = float('inf')
    for i in range(1,N-1):
        for j in range(i+1, N):
            count = 0
            W = ''.join(case[0:i]).count('W')
            B = ''.join(case[i:j]).count('B')
            R = ''.join(case[j:]).count('R')
            count += M*i - W
            count += M*(j-i) - B
            count += M*(N-j) - R
            if ans > count:
                ans = count

    print(f"#{tc} {ans}")