T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    a = list(map(int,input().split()))
    sum = []
    for i in range(M-1,len(a)):
        temp = 0
        for j in range(M):
            temp += a[i-j]
        sum.append(temp)

    result = max(sum)-min(sum)

    print(f"#{tc} {result}")
