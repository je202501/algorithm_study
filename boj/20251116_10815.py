N = int(input())
num1 = list(map(int,input().split()))
M = int(input())
num2 = list(map(int,input().split()))

s = set(num1)

result = []

for i in range(M):
    if num2[i] in s:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i,end=' ')