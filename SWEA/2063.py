T = int(input())


a = list(map(int,input().split()))
a.sort()

center = int(T//2)

result = a[center]

print(result)
