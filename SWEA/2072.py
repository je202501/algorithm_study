T = int(input())
result = [0]*T
for test_case in range(1,T+1):
    a = list(map(int, input().split()))
    result[test_case - 1] = 0
    for i in a:
        if (i%2):
            result[test_case - 1] += i

for i in range(len(result)):
    print('#{} {}'.format(i+1,result[i]))