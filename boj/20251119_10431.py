P = int(input())

for tc in range(1,P+1):
    std = list(map(int,input().split()))
    ans = 0

    for i in range(1,21):
        temp = std[i]
        for j in range(i+1,21):
            if std[i] > std[j]:
                ans += 1

    print(tc,ans)