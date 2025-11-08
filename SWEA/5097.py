from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    num = list(map(int,input().split()))
    queue = deque(num)

    for i in range(M):
        v = queue.popleft()
        queue.append(v)

    v = queue.popleft()
    print(f"#{tc} {v}")