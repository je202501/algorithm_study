T=int(input())

for tc in range(1,T+1):
    No = int(input())
    Num = list(map(int,input().split()))
    di = {}
    temp = 0
    result = 0

    for i in Num:
        if i in di:
            di[i]+=1
        else:
            di[i]=1

    for i in di:
        if di[i]>temp:
            temp = di[i]
            result = i

    print(f'#{No} {result}')


