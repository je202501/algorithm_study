T=int(input())

grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for tc in range(1,T+1):
    N,K=map(int,input().split())
    student = [list(map(int,input().split())) for _ in range(N)]
    score = []
    result = []

    for std in range(N):
        temp = [student[std][0]*0.35 + student[std][1]*0.45 + student[std][2]*0.2,std]
        score.append(temp)

    sorted_score = sorted(score,reverse=True)

    a = 0
    b = 0
    while a<10:
        for i in range(N//10):
            temp = (sorted_score[b][1],grade[a])
            result.append(temp)
            b+=1
        a += 1

    for i in range(N):
        if (K-1) == result[i][0]:
            print(f"#{tc} {result[i][1]}")

