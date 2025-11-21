K, S, N = map(str, input().split())
N = int(N)
M = []
CM = [[0 for _ in range(1, 9)] for _ in range(1, 9)]
KR = ord(K[:1]) - 64
KC = int(K[1:])
SR = ord(S[:1]) - 64
SC = int(S[1:])

move_c = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
move = [[0, 1], [0, -1], [-1, 0], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for _ in range(N):
    temp = input()
    for i in range(8):
        if temp == move_c[i]:
            M.append(move[i])
            break

for i in range(N):
    KR_nx = KR + M[i][1]
    KC_nx = KC + M[i][0]
    SR_nx = SR + M[i][1]
    SC_nx = SC + M[i][0]

    if KR_nx < 1 or KR_nx > 8 or KC_nx < 1 or KC_nx > 8:
        continue
    elif KR_nx == SR and KC_nx == SC:
        if SR_nx < 1 or SR_nx > 8 or SC_nx < 1 or SC_nx > 8:
            continue
        else:
            KR, KC, SR, SC = KR_nx, KC_nx, SR_nx, SC_nx
    else:
        KR, KC = KR_nx, KC_nx

K_ans = chr(KR+64)+str(KC)
S_ans = chr(SR+64)+str(SC)

print(K_ans)
print(S_ans)