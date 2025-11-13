num = int(input())
paper = [[0]*102 for _ in range(102)]

for _ in range(num):
    x, y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1

result = 0
for i in range(1,101):
    for j in range(1,101):
        if paper[i][j] == 0:
            pass
        else:
            if paper[i+1][j] == 0 or paper[i-1][j] == 0:
                result += 1
            if paper[i][j+1] == 0 or paper[i][j-1] == 0:
                result += 1

print(result)