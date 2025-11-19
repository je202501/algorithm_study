N = int(input())
line = list(map(int, input().split()))
a_arr = [n for n in range(1,N+1)]

for i in range(N):
    loc, std = line[i], a_arr[i]
    for j in range(i,i-loc,-1):
        a_arr[j] = a_arr[j-1]
    a_arr[i-loc]=std

print(*a_arr)
