T = int(input())

def fact(n):
    num = 1
    for i in range(2,n+1):
        num *= i
    return num

for tc in range(1,T+1):
    N,M=map(int,input().split())
    result = fact(M) // (fact(N) * fact(M-N))
    print(result)