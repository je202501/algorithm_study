T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    max_value = max(a)
    min_value = min(a)
    result = max_value-min_value
    print(f"#{tc} {result}")