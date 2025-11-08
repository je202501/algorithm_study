T = 10

for tc in range(1,T+1):
    D = int(input())
    height = list(map(int,input().split()))
    result = 0

    for i in range(D):
        max_height = max(height)
        min_height = min(height)
        if (max_height - min_height <= 1):
            break
        max_index = height.index(max_height)
        min_index = height.index(min_height)
        height[max_index] -= 1
        height[min_index] += 1

        result = max(height) - min(height)

    print(f"#{tc} {result}")