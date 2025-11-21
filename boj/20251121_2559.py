N, K = map(int, input().split())
tem = list(map(int, input().split()))
sum_t = sum(tem[:K])
mx = sum_t
for i in range(1, N-K+1):
    sum_t = sum_t + tem[i+K-1] - tem[i-1]
    if mx < sum_t:
        mx = sum_t


print(mx)