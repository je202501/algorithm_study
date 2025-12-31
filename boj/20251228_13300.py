N, K = map(int,input().split())
F = []
M = []
for i in range(N):
    S,Y = map(int,input().split())
    if S == 0:
        F.append(Y)
    else:
        M.append(Y)

F.sort()
M.sort()
result = 0
if len(F) != 0:
    count = 1
    now = F[0]
    for i in range(len(F)):
        if i == 0:
            result +=1
        elif now == F[i]:
            count += 1
        else:
            now = F[i]
            count = 1
            result += 1
        if count > K:
            result += 1
            count = 1

if len(M) != 0:
    count = 1
    now = M[0]
    for i in range(len(M)):
        if i == 0:
            result +=1
        elif now == M[i]:
            count += 1
        else:
            now = M[i]
            count = 1
            result += 1
        if count > K:
            result += 1
            count = 1

print(result)