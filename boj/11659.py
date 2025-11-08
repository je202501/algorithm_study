import sys
input = sys.stdin.readline

N,M = map(int,input().split())

num = list(map(int,input().split()))

prefix_sum = [0]*(N+1)
prefix_sum[0] = 0

for a in range(1,N+1):
    prefix_sum[a] = prefix_sum[a-1]+num[a-1]

for _ in range(M):
    i, j = map(int, input().split())
    part_sum = prefix_sum[j] - prefix_sum[i - 1]
    print(part_sum)

