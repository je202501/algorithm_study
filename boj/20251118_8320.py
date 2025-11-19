n = int(input())
ans = 0
for i in range(1,n+1):
    N = n//i - (i-1)
    if N<1:
        break
    ans += N
print(ans)