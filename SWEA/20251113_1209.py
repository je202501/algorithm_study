T = 10

for tc in range(1,T+1):
    testcase = int(input())
    nums = []
    for _ in range(100):
        nums.append([i for i in map(int,input().split())])
    hap = []
    #가로 합 구하기
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += nums[i][j]
        hap.append(temp)

    #세로 합 구하기
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += nums[j][i]
        hap.append(temp)

    #\대각선 합 구하기
    temp = 0
    for i in range(100):
        temp += nums[i][i]
        hap.append(temp)

    #/대각선 합 구하기
    temp = 0
    for i in range(100):
        temp += nums[99-i][i]
        hap.append(temp)

    print(f"#{tc} {max(hap)}")