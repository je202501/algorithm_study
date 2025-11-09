N, M = map(int,input().split())
location = list(map(int,input().split()))
result = 0

for i in range(M):
    if location[i] == 1:
        for j in range(i,M):
            pass
    elif location[i] > (N+1)//2:
        plus = N - location[i] + 1
        for j in range(i,M):
            location[j] += plus
            if location[j] > N:
                location[j] -= N
        result += plus
    else:
        minus = location[i] - 1
        for j in range(i, M):
            location[j] -= minus
            if location[j] < 1:
                location[j] += N
        result += minus

    for j in range(i + 1, M):
        location[j] -= 1
        if location[j] < 1:
            location[j] += N
    N -= 1


print(result)