N = int(input())
lst = [0]*1001
mx_h = 0
mx_i = 0
h = 0
w = 0
ans = 0

for _ in range(N):
    L, H = map(int,input().split())
    lst[L] = H
    if mx_h < H:
        mx_h = H
        mx_i = L

#왼
for i in range(1,mx_i+1):
    if lst[i] > h:
        h = lst[i]
    ans += h

h = 0
#오
for i in range(1000,mx_i,-1):
    if lst[i] > h:
        h = lst[i]
    ans += h


print(ans)