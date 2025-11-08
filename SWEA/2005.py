T = int(input())

for tc in range(1,T+1):
    N = int(input())
    triangle = [[0,1,0]]
    for i in range(N):
        temp = []
        for j in range(len(triangle[i])):
            if j==0:
                temp.append(0)
            else:
                temp.append(triangle[i][j-1]+triangle[i][j])
        temp.append(0)
        triangle.append(temp)
    print(f"#{tc}")
    for i in range(N):
        for j in triangle[i]:
            if j != 0:
                print(j,end=' ')
        print()

