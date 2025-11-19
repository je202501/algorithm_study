L = int(input())
N = int(input())
pre_mx = 0
pre_mx_val = 0
mx = 0
mx_val = 0
cake = [0 for _ in range(L)]
want = []

for i in range(N):
    temp = list(map(int,input().split()))
    if temp[1]-temp[0]+1 > pre_mx_val:
        pre_mx = i+1
        pre_mx_val = temp[1]-temp[0]+1
    want.append(temp)

for i in range(N):
    st = want[i][0]-1
    fin = want[i][1]
    for j in range(st, fin):
        if cake[j] == 0:
            cake[j] = i+1

for i in range(1, N+1):
    cnt = cake.count(i)
    if cnt > mx_val:
        mx = i
        mx_val = cnt

print(pre_mx)
print(mx)