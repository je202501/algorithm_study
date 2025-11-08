T = int(input())

result=[]

for test_case in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    max = 0
    max_num = 0
    start = 0
    sum = 0
    while max_num < len(price):
        for i in range(max_num,len(price)):
            if price[i] > max:
                max = price[i]
                max_num = i

        for i in range(start,max_num):
            sum += max - price[i]

        start = max_num + 1
        max_num += 1
        max = 0


    result.append(sum)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')