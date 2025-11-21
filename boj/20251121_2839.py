N = int(input())
ans_ck = 0
cnt_3 = 0
cnt_5 = 0
while ans_ck == 0:
    if 3 * cnt_3 > N:
        ans_ck = -1
    temp = N - (3*cnt_3)
    if temp % 5 == 0:
        cnt_5 = temp//5
        ans_ck = 1
    else:
        cnt_3 += 1

if ans_ck == -1:
    print(-1)
else:
    print(cnt_3+cnt_5)
