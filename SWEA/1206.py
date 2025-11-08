T = 10

for tc in range(1,T+1):
    N = int(input())
    building = list(map(int,input().split()))
    result = 0
    for i in range(2,len(building)-2):
        max = 0
        sum = 0
        for j in range(i-2,i+3):
            if j == i:
                continue
            if max < building[j]:
                max = building[j]
        sum = building[i] - max
        if sum > 0:
            result += sum

    print(f"#{tc} {result}")
