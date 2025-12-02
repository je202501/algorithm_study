ans = 0
for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if x1 > p2 or p1 < x2 or y1 > q2 or q1 < y2:
        ans = 'd'
    elif x1 == p2 or p1 == x2:
        if y1 == q2 or q1 == y2:
            ans = 'c'
        else:
            ans = 'b'
    elif y1 == q2 or q1 == y2:
        ans = 'b'
    else:
        ans = 'a'

    print(ans)