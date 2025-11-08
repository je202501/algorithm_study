T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    primes = [2, 3, 5, 7, 11]
    counts = []

    for p in primes:
        cnt = 0
        while N % p == 0:
            N //= p
            cnt += 1
        counts.append(cnt)

    print(f"#{test_case} {' '.join(map(str, counts))}")