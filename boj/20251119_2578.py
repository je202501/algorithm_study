num1 = [[i for i in map(int, input().split())]for _ in range(5)]
num2 = []

for _ in range(5):
    line = input().strip()
    number = list(map(int, line.split()))
    num2.extend(number)



ans = 0
for n in range(len(num2)):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if num1[i][j] == num2[n]:
                num1[i][j] = 0
    #가로 세로
    for i in range(5):
        col_sum = sum(num1[r][i] for r in range(5))

        if sum(num1[i]) == 0:
            cnt += 1
        if col_sum == 0:
            cnt += 1
    cnt2 = 0
    cnt3 = 0
    #대각선
    for i in range(5):
        if num1[i][i] ==0:
            cnt2 +=1
        if num1[i][4-i] ==0:
            cnt3 +=1
    if cnt2 == 5:
        cnt += 1
    if cnt3 == 5:
        cnt += 1
    if cnt >= 3:
        ans = n+1
        break

print(ans)