T = int(input())
result = []

for test_case in range (1,T+1):
    a = list(map(int,input().split()))
    sum = 0
    for i in a:
        sum += i
    result.append(sum/len(a))

for i in range(len(result)):
    print('#{} {}'.format(i+1,round(result[i])))