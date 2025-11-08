from collections import Counter

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = list(input())

    cnt = Counter(a)
    result = max(cnt, key = lambda x: (cnt[x],x))
    frequency = cnt[result]

    print(f'#{tc} {result} {frequency}')

