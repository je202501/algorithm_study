T = int(input())

for tc in range(1,T+1):
    C = int(input())
    change = [25,10,5,1]
    result = [0,0,0,0]

    for i in range(len(change)):
        result[i] = C // change[i]
        C %= change[i]

    for i in result:
        print(i,end=' ')