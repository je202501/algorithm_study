T = int(input())

result = [1]
mul = 1
for test_case in range(1,T+1):
    mul *= 2
    result.append(mul)

for i in result:
    print(i,end=" ")

