w, h = map(int, input().split())
n = int(input())
col = [0, w]
row = [0, h]
c_mx = 0
r_mx = 0
for i in range(n):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        col.append(temp[1])
    elif temp[0] == 0:
        row.append(temp[1])

col.sort()
row.sort()

for i in range(1,len(col)):
    temp = col[i] - col[i-1]
    if c_mx < temp:
        c_mx = temp

for i in range(1,len(row)):
    temp = row[i] - row[i-1]
    if r_mx < temp:
        r_mx = temp

ans = c_mx*r_mx

print(ans)
