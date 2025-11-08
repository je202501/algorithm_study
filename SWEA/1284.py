T = int(input())

for tc in range(1,T+1):
    P,Q,R,S,W = map(int,input().split())

    A = W*P
    if W<R :
        B = Q
    else:
        B = Q+(W-R)*S

    if A<B:
        print(f"#{tc} {A}")
    else:
        print(f"#{tc} {B}")