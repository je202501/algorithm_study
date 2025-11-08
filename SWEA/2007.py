T=int(input())
for tc in range(1,T+1):
    arr=list(input())
    s=arr[0]
    N=len(arr)
    ans=0
    for i in range(1,N-1):
        if s==arr[i] and arr[:i]==arr[i:2*i]:
            ans=i
            break
    print(f'#{tc} {ans}')