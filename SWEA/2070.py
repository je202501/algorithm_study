T=int(input())

result = []

for test_case in range(1, T+1):
    a,b = map(int,input().split())
    if a<b:
        result.append('<')
    elif a == b:
        result.append('=')
    elif a>b:
        result.append('>')

for i in range(len(result)):
    print('#{} {}'.format(i+1,result[i]))