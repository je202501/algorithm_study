T = int(input())

for tc in range(1,T+1):
    N = list(input())
    M = input()

    N = set(N)
    dic = {}
    for a in N:
        dic[a] = 0

    for a in M:
        if a in dic:
            dic[a] += 1

    max = 0
    for a in dic:
        if dic[a] > max:
            max = dic[a]

    print(f"#{tc} {max}")